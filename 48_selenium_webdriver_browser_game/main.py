from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

price_whole= driver.find_element(By.CLASS_NAME, "a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(f"Price: {price_whole.text}.{price_fraction.text} €")

driver.quit()