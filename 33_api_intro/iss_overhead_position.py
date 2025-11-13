import requests

#Header needed to get access to API endpoints blocking non-browser API calls
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0'}

#ISS position
response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
response_iss.raise_for_status()

data_iss = response_iss.json()

longitude_iss = data_iss["iss_position"]["longitude"]
latitude_iss = data_iss["iss_position"]["latitude"]
position_iss = (float(latitude_iss), float(longitude_iss))

#Location resolution
response_address = requests.get(url=f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude_iss}"
                                    f"&lon={longitude_iss}&accept-language=en", headers=headers)
response_address.raise_for_status()

data_address = response_address.json()

try:
    country = data_address["address"]["country"]
    state = data_address.get("address").get("state")
    village = data_address.get("address").get("village", "")
except KeyError:
    print(f"{data_address["error"]} {position_iss} - The ISS is probably located over the ocean.")
else:
    if village != "":
        print(f"The ISS is currently located over {village}, in the state of {state}, in {country}.")
    else:
        print(f"The ISS is currently located over the state {state}, {country}.")