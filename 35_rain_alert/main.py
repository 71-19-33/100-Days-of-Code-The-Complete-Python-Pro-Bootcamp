import requests, os
from twilio.rest import Client

#owm parameters
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
owm_parameters = {
    "lat": 52.520008,
    "lon": 13.404954,
    "appid": os.environ["OPENWEATHERMAP_TOKEN"],
    "units": "metric",
    "cnt": 5
}

#owm api call configuration
owm_api = requests.get(owm_endpoint, params=owm_parameters)
owm_api.raise_for_status()
weather_json = owm_api.json()

#owm data configuration
weather_data = weather_json["list"]

#twilio parameters
account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_TOKEN"]
twilio_nr = "+17439626778"
client = Client(account_sid, auth_token)


def send_sms(body):
    client.messages.create(body=body, from_=twilio_nr, to=os.environ["MY_PHONE_NUMBER"])

#check for rain
def check_for_rain():
    for timestamp in weather_data:
        weather_id = timestamp["weather"][0]["id"]
        if int(weather_id) < 700:
            alert = "It is or will be raining soon. Pack your umbrella!"
        else:
            alert = "No need for an umbrella soon."
    print(alert)
    send_sms(alert)

check_for_rain()
