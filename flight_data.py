# handles the structuring of the flight data

class FlightData: 
    
    def __init__(self, airport_code, flight_info):
        self.price = 0 
        self.departure_airport_code = airport_code
        self.flight_info = flight_info 
        
