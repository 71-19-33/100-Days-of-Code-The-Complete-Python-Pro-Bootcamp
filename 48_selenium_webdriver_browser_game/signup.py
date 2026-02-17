from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Max")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Mustermann")

mail = driver.find_element(By.NAME, "email")
mail.send_keys("mustermann_max@testmail.com")

button = driver.find_element(By.CSS_SELECTOR, "body > form > button")
button.click()

driver.quit()