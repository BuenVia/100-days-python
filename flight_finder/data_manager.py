import requests

sheety_endpoint = "https://api.sheety.co/1b44c2fc74da196fc5e0fa22856b14ca/flightDeal/sheet1"

class DataManager:

    def __init__(self):
        self.sheet_data = {}

    def get_sheet_data(self):
        response = requests.get(sheety_endpoint)
        data = response.json()['sheet1']
        return data
    
