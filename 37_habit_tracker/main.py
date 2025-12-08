import requests

TOKEN = "notsosecret"
USERNAME = "uetzemuetze"

#--- pixela user endpoint
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

pixela_endpoint = "https://pixe.la/v1/users"

# pixela_response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(pixela_response.text)

#--- pixela graphs endpoint
pixela_parameters_graphs = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "kuro"
}

pixela_headers = {
    "X-USER-TOKEN": TOKEN,
}

pixela_endpoint_graphs = f"{pixela_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=pixela_endpoint_graphs, json=pixela_parameters_graphs, headers=pixela_headers)
# print(response.text)