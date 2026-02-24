from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os
from datetime import date, timedelta

#credentials
ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"

#global variables
COUNTER_BOOKINGS = 0
COUNTER_WAITLISTS = 0
COUNTER_NOJOB = 0
COURSES_PROCESSED = ""

#calculate desired date
def find_date(weekday_desired: int):
    date_now = date.today()
    weekday_now = date_now.weekday()
    weekday_difference = abs(weekday_desired - weekday_now)
    date_desired = date_now + timedelta(days=weekday_difference)
    return date_desired

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

#interact with any event on a given weekday at a given time
def book_any_event(day_desired: int, time_desired: int):
    global COUNTER_NOJOB, COUNTER_BOOKINGS, COUNTER_WAITLISTS, COURSES_PROCESSED
    date_desired = find_date(day_desired)
    date_desired_events = driver.find_elements(By.CSS_SELECTOR, f"[id*='{date_desired}-{time_desired}']")
    ##find details
    for entry in date_desired_events:
        try:
            class_title = entry.find_element(By.TAG_NAME, "h3").text
            booking_button = entry.find_element(By.CSS_SELECTOR, f"button[id*='{time_desired}']")
            course_description = f"{class_title} on {date_desired}"
            if booking_button.text == "Book Class":
                booking_button.click()
                event = "✓ Booked:"
                event_type = "• [New Booking]"
                COUNTER_BOOKINGS += 1
            elif booking_button.text == "Join Waitlist":
                booking_button.click()
                event = "✓ Joined Waitlist:"
                event_type = "• [New Waitlist]"
                COUNTER_WAITLISTS += 1
            elif booking_button.text == "Waitlisted":
                event = "✓ Already on Waitlist:"
                event_type = "• [Already on Waitlist]"
                COUNTER_NOJOB += 1
            else:
                event = "✓ Already booked:"
                event_type = "• [Already Booked]"
                COUNTER_NOJOB += 1
            break
        except:
            continue
    print(f"{event} {course_description}")
    COURSES_PROCESSED += f"{event_type} {course_description}\n"

#interact with an event next tuesday 6pm => tue 6pm not available, wednesday is used
book_any_event(1, 1800)
book_any_event(3, 1800)

#print summary
print(f"""\n
--- BOOKING SUMMARY ---
Classes booked: {COUNTER_BOOKINGS}
Waitlists joined: {COUNTER_WAITLISTS}
Already booked/waitlisted: {COUNTER_NOJOB}
Total classes processed: {COUNTER_BOOKINGS+COUNTER_WAITLISTS+COUNTER_NOJOB}""")
print(f"""\n
--- DETAILED CLASS LIST ---
{COURSES_PROCESSED}""")

#close the driver
#driver.quit()