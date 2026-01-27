import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
import os

URL = "https://appbrewery.github.io/instant_pot/"
#target price in $ with two decimal places
TARGET = 100.00

#sending sms instead of mail, following are twilio parameters
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
twilio_nr = "+17439626778"
client = Client(account_sid, auth_token)

def send_sms(body):
    client.messages.create(body=body, from_=twilio_nr, to=os.getenv("MY_PHONE_NUMBER"))

#scrape page with beautiful soup
request = requests.get(f"{URL}")
request.raise_for_status()
page_content = BeautifulSoup(request.text, "html.parser")

#find the amazon item price
price_tag = page_content.find(class_="aok-offscreen")
price = price_tag.get_text().split("$")[1].strip()

#find the amazon item title
title_tag = page_content.select_one("#productTitle")
title = title_tag.get_text().replace("                                        ", " ").replace("\r", " ").strip()

def price_check():
    if float(price) < TARGET:
        message = f"{title} is now ${price} at {URL}."
        send_sms(message)

price_check()
