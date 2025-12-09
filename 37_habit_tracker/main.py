import requests
from datetime import datetime

TOKEN = "notsosecret123"
USERNAME = "uetzemuetze"

#--- format time to pixela format yyyyMMdd
def format_date(input_year: int, input_month: int, input_day: int):
    date = datetime(year=input_year, month=input_month, day=input_day).strftime("%Y%m%d")
    return date

#--- pixela user endpoint, creating a user
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_endpoint = "https://pixe.la/v1/users"

# pixela_response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(pixela_response.text)

#--- pixela graphs endpoint, creating a graph
graph_parameters = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "kuro"
}

pixela_header = {
    "X-USER-TOKEN": TOKEN,
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=pixela_header)
# print(response.text)

#--- add data to the graph
#--- prepare date and quantity fir pixel manipulation
def define_pixel(input_year: int, input_month: int, input_day: int, quantity: str):
    date = format_date(input_year, input_month, input_day)
    parameters = {
        "date": date,
        "quantity": quantity
    }
    return parameters

def pixel_manipulation(input_year: int, input_month: int, input_day: int, option = "post", quantity = "0"):
    """
    option = post / put / delete
    """

    pixel_parameters = define_pixel(input_year, input_month, input_day, quantity)
    pixel_endpoint_post = f"{graph_endpoint}/{graph_parameters["id"]}"
    pixel_endpoint_put = f"{graph_endpoint}/{graph_parameters["id"]}/{pixel_parameters["date"]}"

    if option == "delete":
        pixel_change = requests.delete(pixel_endpoint_put, headers=pixela_header)
    elif option == "put":
        pixel_change = requests.put(pixel_endpoint_put, json=pixel_parameters, headers=pixela_header)
    else:
        pixel_change = requests.post(pixel_endpoint_post, json=pixel_parameters, headers=pixela_header)
    print(pixel_change.text)
#pixel_manipulation(2025,10,7, "post", "60.3")
#pixel_manipulation(2025,10,7, "delete")

#--- manipulations before refactoring
#add_pixel("20251209", "10.5")
#add_pixel(2025,11,6, "25.1")
#change_pixel(2025, 11, 6, "8.3")

#--- guided user input
user_year = int(input("For which year would you like to enter data (yyyy): "))
user_month = int(input("For which month would you like to enter data (mm): "))
user_day = int(input("For which day would you like to enter data (dd): "))
user_distance = input("How many kilometers did you cycle at that day (float): ")

pixel_manipulation(user_year, user_month, user_day, quantity=user_distance)