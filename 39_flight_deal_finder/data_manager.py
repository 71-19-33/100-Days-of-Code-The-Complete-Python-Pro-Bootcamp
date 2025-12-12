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

    def edit_data(self, line_to_change: str, column_to_change: str, value_to_change: str):
        edit_endpoint = f"{self.endpoint}/{line_to_change}"
        parameters = {
            "price": {
                f"{column_to_change}": f"{value_to_change}",
            }
        }
        write = requests.put(edit_endpoint, headers=self.headers, json=parameters)
        write.raise_for_status()
        if write.status_code == 200:
            print(f"Successfully updated \"{value_to_change}\" in line: {line_to_change} / column: {column_to_change}")