import requests, os

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = SHEETY_ENDPOINT
        self.headers = {
            "Authorization": "Bearer " + SHEETY_TOKEN,
        }

    def get_data(self):
        read = requests.get(self.endpoint, headers=self.headers)
        read.raise_for_status()
        data = read.json()
        return data

    def edit_data(self, column_to_change, value_to_change):
        data = self.get_data()
        for entries in data["prices"]:
            object_id = str(entries["id"])
            edit_endpoint = f"{self.endpoint}/{object_id}"
            parameters = {
                "price": {
                    f"{column_to_change}": f"{value_to_change}",
                }
            }
            write = requests.get(edit_endpoint, headers=self.headers, params=parameters)
            write.raise_for_status()
        print("Data successfully updated")