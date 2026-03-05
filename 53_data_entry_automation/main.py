import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_SHEET_URL = "https://docs.google.com/forms/d/e/1FAIpQLSffGs40h7U8GPQKZ81p8zp0-NTgp8binEqxFNd4GaSpmVbnQQ/viewform"
HEADER = {
    "Accept-Language": "de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,it;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
}

#scrape page with beautiful soup
request = requests.get(f"{ZILLOW_URL}", headers=HEADER)
request.raise_for_status()
page_content = BeautifulSoup(request.text, "html.parser")

#listings: create list of links
links_tag = page_content.find_all("a", class_="StyledPropertyCardDataArea-anchor")
links = [link.get("href") for link in links_tag]

#listings: create list of prices, cleaned up by removal of some characters
prices_tag = page_content.find_all(class_="PropertyCardWrapper__StyledPriceLine")
prices = [price.get_text().strip("+/mo 1bd") for price in prices_tag]
## refactor faulty formats, e.g. 1914 to 1,914
for price in prices:
    if price[2] != ",":
        string_list = list(price)
        string_list.insert(2, ",")
        price = "".join(string_list)

#listings: create list of addresses
addresses_tag = page_content.find_all("address")
addresses = [address.get_text().strip(" \n").replace("|", ",").split(", ", 1)[1] for address in addresses_tag]

#initialize webdriver
driver = webdriver.Firefox()
driver.get(GOOGLE_SHEET_URL)


for i in range(len(links)):
    time.sleep(3)
    #find the form inputs
    address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address_field.send_keys(addresses[i])
    price_field.send_keys(prices[i])
    link_field.send_keys(links[i])
    send_button.click()
    time.sleep(3)
    additional_answers = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    additional_answers.click()

driver.quit()