import requests
from flight_data import FlightData

API_KEY = "rNC69JGbGRhOJHV4bcKVkyI4Zj4YvXwH"

tequila_endpoint = "https://tequila-api.kiwi.com"

class FlightSearch:

    def get_destination_code(self, city):
        locations_endpoint = f"{tequila_endpoint}/locations/query"
        headers = {"apikey": API_KEY}
        parameters = {"term": city, "location_types": "city"}
        response = requests.get(url=locations_endpoint, headers=headers, params=parameters)
        results = response.json()['locations']
        return results[0]['code']
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(
            url=f"{tequila_endpoint}/v2/search",
            headers=headers,
            params=query
        )

        try:
            data = response.json()["data"][0]
        except:
            print(f"No flights found for {destination_city_code}")
            return None
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
            out_airline=data["route"][0]["airline"],
            out_airline_no=data["route"][0]["flight_no"],
            return_airline=data["route"][1]["airline"],
            return_airline_no=data["route"][1]["flight_no"]
        )
        return flight_data