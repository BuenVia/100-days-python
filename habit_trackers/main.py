import requests

USERNAME = "mattc" 
TOKEN = "championsleague"
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

respose = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(respose.text)

# graph_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

# graph_details = {
#     "date": "20230214",
#     "quantity": "1",
# }

# response = requests.post(url=graph_endpoint, json=graph_details, headers=headers)
# print(response.text)