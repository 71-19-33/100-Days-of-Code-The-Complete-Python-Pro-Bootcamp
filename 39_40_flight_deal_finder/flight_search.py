import requests, os, datetime, dateutil.relativedelta, copy
from flight_data import FlightData

api_mock = FlightData()

ORIGIN = "LON"
tomorrow = (datetime.datetime.now() + datetime.timedelta(days=+1)).strftime("%Y-%m-%d")
in_six_months = (datetime.datetime.now() + datetime.timedelta(days=+183)).strftime("%Y-%m-%d")

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
        self.cheapest_date_endpoint = "https://test.api.amadeus.com/v1/shopping/flight-dates"

# token is valid for 30 minutes, one could implement a timer, that requests a new token after running out
    def get_token(self):
        request = requests.post(self.token_endpoint, data=self.token_body, headers=self.token_headers)
        request.raise_for_status()
        data = request.json()
        token = str(data["access_token"])
        return token

    def get_iata_city_codes(self, city_list: list):
        iata_city_codes = []
        for city in city_list:
            cities_parameters = {"keyword": f"{city.upper()}"}
            request = requests.get(self.city_endpoint, params=cities_parameters, headers=self.auth_headers)
            request.raise_for_status()
            data = request.json()
            iata_city_code = data["data"][0]["iataCode"]
            iata_city_codes.append(iata_city_code)
        return iata_city_codes

    def find_cheapest_date(self, iata_price_pair: dict):
        """

        :param iata_price_pair: As dict with iataCode and price
        :return:
        """
        date_list = []
        for entry in iata_price_pair:
            cheapest_date_parameters = {
                "origin": ORIGIN,
                "destination": entry,
                "departureDate": f"{tomorrow},{in_six_months}",
                "maxPrice": iata_price_pair[entry],
            }
            try:
                [cheapest_flight] = api_mock.generate_answer(cheapest_date_parameters)["data"]
                date_list.append(copy.deepcopy(cheapest_flight))
            except TypeError:
                pass
        return date_list
