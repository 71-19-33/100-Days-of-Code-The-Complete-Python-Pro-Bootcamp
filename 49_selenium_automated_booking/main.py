from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os
import calendar
from datetime import date, timedelta, datetime

#credentials
ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"

#global variables
COUNTER_BOOKINGS = 0
COUNTER_BOOKINGS_FOUND = 0
COUNTER_WAITLISTS = 0
COUNTER_NOJOB = 0
COURSES_PROCESSED = ""
COURSES_VERIFIED = ""

#calculate desired date
def find_date(query_weekday: str):
    query_weekday_nr = list(calendar.day_name).index(query_weekday)
    today = date.today()
    today_weekday_nr = today.weekday()
    weekday_difference = (query_weekday_nr - today_weekday_nr) % 7
    date_desired = today + timedelta(days=weekday_difference)
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

#webpage: login
login = driver.find_element(By.ID, "login-button")
login.click()

#webpage: enter credentials
mail_field = driver.find_element(By.ID, "email-input")
mail_field.send_keys(ACCOUNT_EMAIL)
mail_field = driver.find_element(By.ID, "password-input")
mail_field.send_keys(ACCOUNT_PASSWORD, Keys.RETURN)

#webpage: wait for schedule
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "schedule-page")))

#webpage: interact with any event on a given weekday at a given time
def book_any_event(class_weekday: str, class_time: str):
    global COUNTER_NOJOB, COUNTER_BOOKINGS, COUNTER_WAITLISTS, COURSES_PROCESSED, COURSES_VERIFIED, COUNTER_BOOKINGS_FOUND
    date_desired = find_date(class_weekday)
    date_desired_events = driver.find_elements(By.CSS_SELECTOR, f"[id*='{date_desired}-{class_time}']")
    
    #find class titles and times and interact with event, provide result
    for entry in date_desired_events:
        try:
            class_title = entry.find_element(By.TAG_NAME, "h3").text
            booking_button = entry.find_element(By.CSS_SELECTOR, f"button[id*='{class_time}']")
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
    
    #verify that booking appears on the my bookings page by going to the bookings page
    try:
        my_bookings_button = driver.find_element(By.ID, "my-bookings-link")
        my_bookings_button.click()
        my_booked_courses = driver.find_elements(By.CSS_SELECTOR, "[id*='booking-card-booking'] > div > p:nth-child(2)")
    except:
        pass
    #search through found courses, reformat date and time queries
    query_date = f"{date_desired.strftime('%a')}, {date_desired.strftime('%b')} {date_desired.day}, "
    query_time_raw = datetime.strptime(class_time, "%H%M")
    query_time = query_time_raw.strftime("%I:%M %p").lstrip("0")
    query_date_time = f"{query_date}{query_time}"
    #find courses in my_booked_courses:
    for course in my_booked_courses:
        if query_date_time in course.text:
            COURSES_VERIFIED += f"✓ Verified: {class_title} {event_type}\n"
            COUNTER_BOOKINGS_FOUND += 1
        else:
            pass

    #going back to the schedule page
    try:
        my_schedule_button = driver.find_element(By.ID, "schedule-link")
        my_schedule_button.click()
    except:
        pass


#webpage: interact with an event next tuesday 6pm + next thursday 6pm
book_any_event(class_weekday="Tuesday", class_time="1800")
book_any_event(class_weekday="Thursday", class_time="1800")

#print summary
# --- BOOKING SUMMARY ---
# Classes booked: {COUNTER_BOOKINGS}
# Waitlists joined: {COUNTER_WAITLISTS}
# Already booked/waitlisted: {COUNTER_NOJOB}
print(f"\n--- Total classes processed: {COUNTER_BOOKINGS+COUNTER_WAITLISTS+COUNTER_NOJOB}")
# print(f"""\n--- DETAILED CLASS LIST ---{COURSES_PROCESSED}""")
print(f"\n--- VERIFYING ON MY BOOKINGS PAGE ---\n{COURSES_VERIFIED}")
print(f"--- VERIFICATION RESULT ---\nExpected: {COUNTER_BOOKINGS+COUNTER_WAITLISTS+COUNTER_NOJOB} bookings\nFound: {COUNTER_BOOKINGS_FOUND} bookings.")
if COUNTER_BOOKINGS+COUNTER_WAITLISTS+COUNTER_NOJOB == COUNTER_BOOKINGS_FOUND:
    print("✅ SUCCESS: All bookings verified!")
else:
    print("FAIL: NOT all bookings verified!")


#close the driver
driver.quit()