from data_manager import DataManager
from flight_data import FlightData

data_manager = DataManager()
flight_data = FlightData()

sheet_data = data_manager.get_sheet_data()

if sheet_data[0]['iataCode'] == '':
    for city in sheet_data:
        city['iataCode'] = flight_data.get_iata_codes(city['city'])
        print(city) # Change this to to update the sheet via the FlightData class.