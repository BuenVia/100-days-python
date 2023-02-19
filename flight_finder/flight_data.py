
class FlightData:
    
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, out_airline, out_airline_no, return_airline, return_airline_no):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.out_airline = out_airline
        self.return_airline = return_airline
        self.out_airline_no = out_airline_no
        self.return_airline_no = return_airline_no
