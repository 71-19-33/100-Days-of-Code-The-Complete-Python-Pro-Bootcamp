from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#-----Amazon price scraping:
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# price_whole= driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"Price: {price_whole.text}.{price_fraction.text} €")

#-----Get the event name and date from the website:
driver.get("https://www.python.org/")

event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")

event_schedule = {
    i: {"time": date.text, "name": name.text} for i, (date, name) in enumerate(zip(event_dates, event_names))
}

print(event_schedule)

driver.quit()