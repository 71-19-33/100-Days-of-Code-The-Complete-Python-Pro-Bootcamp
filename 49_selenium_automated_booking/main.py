from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os
from time import sleep, time

#credentials
ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"

#configure firefox profile
user_data_dir = os.path.join(os.getcwd(), "firefox_profile")
options = Options()
options.add_argument(f"--user-data-dir={user_data_dir}")
firefox_profile = FirefoxProfile()
options.profile = firefox_profile

#initialize webdriver
driver = webdriver.Firefox(options=options)
driver.get(GYM_URL)

#login
login = driver.find_element(By.ID, "login-button")
login.click()
##enter credentials
mail_field = driver.find_element(By.ID, "email-input")
mail_field.send_keys(ACCOUNT_EMAIL)
mail_field = driver.find_element(By.ID, "password-input")
mail_field.send_keys(ACCOUNT_PASSWORD, Keys.RETURN)

#wait for schedule
schedule = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "schedule-page")))

#book an class next tuesday 6pm
##find days
appointments = driver.find_elements(By.CLASS_NAME, "Schedule_dayGroup__y79__")
##find wednesday, 6pm course
for entry in appointments:
    try:
        wednesday = entry.find_element(By.CSS_SELECTOR, "[id*='wed']")
        course = wednesday.find_element(By.CSS_SELECTOR, "button[id$='-1800']")
        course.click()
        break
    except:
        continue
        
#close the driver
#driver.quit()