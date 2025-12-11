#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
#program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

#initialization
sheet = DataManager()
flight_data = FlightSearch()

#get cities from sheet
cities = [entry["city"] for entry in sheet.get_data()["prices"]]
#['Paris', 'Frankfurt', 'Tokyo', 'Hong Kong', 'Istanbul', 'Kuala Lumpur', 'New York', 'San Francisco', 'Dublin']
#get iata city codes for cities
iata_city_codes = flight_data.get_iata_city_codes(cities)
#['PAR', 'FRA', 'TYO', 'HKG', 'IST', 'KUL', 'NYC', 'SFO', 'DBN']


