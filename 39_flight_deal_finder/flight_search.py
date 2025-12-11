import requests, os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.key = os.environ["AMADEUS_KEY"]
        self.secret = os.environ["AMADEUS_SECRET"]
        self.token_headers = {"Content-Type": "application/x-www-form-urlencoded"}
        self.token_body = {"grant_type": "client_credentials", "client_id": self.key, "client_secret": self.secret}
        self.token = self.get_token()
        self.auth_headers = {"Authorization": f"Bearer {self.token}"}
        self.city_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

    def get_token(self):
        request = requests.post(self.token_endpoint, data=self.token_body, headers=self.token_headers)
        request.raise_for_status()
        data = request.json()
        token = str(data["access_token"])
        return token

    def get_iata_city_codes(self, city_list):
        iata_city_codes = []
        for city in city_list:
            cities_parameters = {"keyword": f"{city.upper()}"}
            request = requests.get(self.city_endpoint, params=cities_parameters, headers=self.auth_headers)
            request.raise_for_status()
            data = request.json()
            iata_city_code = data["data"][0]["iataCode"]
            iata_city_codes.append(iata_city_code)
        return iata_city_codes

