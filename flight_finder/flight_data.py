import requests

API_KEY = "rNC69JGbGRhOJHV4bcKVkyI4Zj4YvXwH"

tequila_endpoint = "https://tequila-api.kiwi.com"

class FlightData:

    def get_iata_codes(self, city):
        locations_endpoint = f"{tequila_endpoint}/locations/query"
        headers = {"apikey": API_KEY}
        parameters = {"term": city, "location_types": "city"}
        response = requests.get(url=locations_endpoint, headers=headers, params=parameters)
        results = response.json()['locations']
        return results[0]['code']