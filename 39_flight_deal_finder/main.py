#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
#program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

#-----initialization
sheet = DataManager()
flights = FlightSearch()
data = FlightData()
notifier = NotificationManager()

#-----get cities from sheet
#cities = [entry["city"] for entry in sheet.get_data()["prices"]]
###solution after first successful attempt, to save api calls
cities = ["Paris", "Frankfurt", "Tokyo", "Hong Kong", "Istanbul", "Kuala Lumpur", "New York", "San Francisco", "Dublin"]

#-----get iata city codes for cities
#iata_city_codes = flights.get_iata_city_codes(cities)
###solution after first successful attempt, to save api calls
iata_city_codes = ["PAR", "FRA", "TYO", "HKG", "IST", "KUL", "NYC", "SFO", "DBN"]

#-----write to sheet
# for code in iata_city_codes:
#     sheet.edit_data(iata_city_codes.index(code)+2, "iataCode", code)
###values written successfully

#-----get price limits
#price_limits = [entry["lowestPrice"] for entry in sheet.get_data()["prices"]]
###solution after first successful attempt, to save api calls
price_limits = [54, 42, 485, 551, 95, 414, 240, 260, 378]

#-----format data as dict to feed into flight finder function
query_data = dict(zip(iata_city_codes, price_limits))

#-----find cheapest flights
#cheapest_flights = flights.find_cheapest_date(query_data)
###solution after first successful attempt
cheapest_flights = [
    {'type': 'flight-date',
     'origin': 'LON',
     'destination': 'FRA',
     'departureDate': '2025-12-16',
     'returnDate': '2026-06-16',
     'price': {'total': '40'}
     },
    {'type': 'flight-date',
     'origin': 'LON',
     'destination': 'SFO',
     'departureDate': '2025-12-16',
     'returnDate': '2026-06-16',
     'price': {'total': '258'}
     }
]

#-----format to sms friendly text
cheapest_flights_sms = data.convert_flight_data_to_sms(cheapest_flights)

for entry in cheapest_flights_sms:
    notifier.send_sms(entry)

