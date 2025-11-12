import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def check_position(iss_latitude, iss_longitude):
    if MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LONG-5 < iss_longitude < MY_LONG+5:
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Europe/Berlin",
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour

def check_visibility(sunrise, sunset, hour):
    if sunset < hour and sunrise < hour:
        return True
    else:
        return False


def send_mail():
    #connection = smtplib.SMTP('smtp.gmail.com', 587)
    #connection.starttls()
    #connection.login("<EMAIL>", "<PASSWORD>")
    #connection.sendmail(
        from_addr="<EMAIL>",
        to_addrs="<EMAIL>",
        msg="Look up! The ISS is above!"
    #)
        print("Mail Sent")
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if check_position(iss_latitude, iss_longitude) and check_visibility(sunrise, sunset, hour):
        send_mail()