import random

class FlightData:
    #Original intent: This class is responsible for structuring the flight data.
    #I will use this class to mock the defunct endpoint
    def __init__(self):
        self.data_point = {
                    "type": "flight-date",
                    "origin": "",
                    "destination": "",
                    "departureDate": "",
                    "returnDate": "",
                    "price": {
                        "total": ""
                    }
                }
        self.answer = {"data": [self.data_point]}


    def generate_answer(self, input_json: dict):
        chance_for_cheaper_flight = 0.1
        if random.random() < chance_for_cheaper_flight:
            origin = input_json["origin"]
            destination = input_json["destination"]
            departure_date_range = input_json["departureDate"].split(",")
            departure_date = departure_date_range[0]
            return_date = departure_date_range[1]
            price_max = input_json["maxPrice"]
            price = str(int(price_max) - random.randint(1, 5))

            self.data_point["origin"] = origin
            self.data_point["destination"] = destination
            self.data_point["departureDate"] = departure_date
            self.data_point["returnDate"] = return_date
            self.data_point["price"]["total"] = price
            return self.answer
        else:
            return None

    def convert_flight_data_to_sms(self, flight_data: list):
        sms_body = []
        for entry in flight_data:
            price = entry["price"]["total"]
            origin = entry["origin"]
            destination = entry["destination"]
            departure_date = entry["departureDate"]
            return_date = entry["returnDate"]
            message = (f"Low price alert! Only €{price} to fly from {origin} to {destination}, "
                       f"on {departure_date} until {return_date}")
            sms_body.append(message)
        return sms_body



