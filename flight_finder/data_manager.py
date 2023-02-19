import requests

sheety_endpoint = "https://api.sheety.co/1b44c2fc74da196fc5e0fa22856b14ca/flightDeal/sheet1"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_desitnation_data(self):
        response = requests.get(sheety_endpoint)
        self.destination_data = response.json()['sheet1']
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data    
            )
            print(response.text)