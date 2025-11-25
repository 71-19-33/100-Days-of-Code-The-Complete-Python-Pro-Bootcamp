import requests
#parameters
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
owm_parameters = {
    "lat": 52.520008,
    "lon": 13.404954,
    "appid": "3fc8e7117ab54915c9c06ae6f471aa57",
    "units": "metric",
    "cnt": 5
}

number_of_timestamps = owm_parameters["cnt"]

#api call configuration
owm_api = requests.get(owm_endpoint, params=owm_parameters)
owm_api.raise_for_status()
weather_json = owm_api.json()

#data configuration
weather_data = weather_json["list"]

#check for rain
def check_for_rain():
    for timestamp in range(number_of_timestamps):
        weather_id = int(weather_data[timestamp]["weather"][0]["id"])
        if weather_id < 700:
            return True
        else:
            return False
print(check_for_rain())
