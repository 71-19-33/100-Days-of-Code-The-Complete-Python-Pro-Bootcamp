import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
import os

URL_STATIC = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
HEADER = {
    "Accept-Language": "de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,it;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
}
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
request = requests.get(f"{URL}", headers=HEADER)
request.raise_for_status()
page_content = BeautifulSoup(request.text, "html.parser")

#find the amazon item price
price_tag = page_content.find(class_="aok-offscreen")
price = price_tag.get_text().split("EUR")[0].strip().replace(",", ".")

#find the amazon item title
title_tag = page_content.select_one("#productTitle")
title = title_tag.get_text().replace("                                        ", " ").replace("\r", " ").strip()

def price_check():
    if float(price) < TARGET:
        message = f"{title} is now {price} € at {URL}."
        send_sms(message)

price_check()
