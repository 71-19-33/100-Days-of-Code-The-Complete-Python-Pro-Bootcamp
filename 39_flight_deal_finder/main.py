#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
#program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

#initialization
sheet = DataManager()
flights = FlightSearch()

#get cities from sheet
#cities = [entry["city"] for entry in sheet.get_data()["prices"]]
###solution after first successful attempt, to save api calls
cities = ["Paris", "Frankfurt", "Tokyo", "Hong Kong", "Istanbul", "Kuala Lumpur", "New York", "San Francisco", "Dublin"]

#get iata city codes for cities
#iata_city_codes = flights.get_iata_city_codes(cities)
###solution after first successful attempt, to save api calls
iata_city_codes = ["PAR", "FRA", "TYO", "HKG", "IST", "KUL", "NYC", "SFO", "DBN"]

#write to sheet
# for code in iata_city_codes:
#     sheet.edit_data(iata_city_codes.index(code)+2, "iataCode", code)
###values written successfully

#500 received -> needs debugging
print(flights.find_cheapest_date("PAR", 54))