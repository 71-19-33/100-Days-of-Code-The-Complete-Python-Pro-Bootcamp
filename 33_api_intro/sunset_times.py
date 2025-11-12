import requests
from datetime import datetime

WOLFSBURG_LAT = 52.427547
WOLFSBURG_LNG = 10.780420

parameters = {
    "lat": WOLFSBURG_LAT,
    "lng": WOLFSBURG_LNG,
    "formatted": 0,
    "tzid": "Europe/Berlin",
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
print(sunrise)
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset)

time_now = datetime.now()
print(time_now.hour)