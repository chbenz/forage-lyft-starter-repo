from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear_sensor):
        self.wear_sensor = wear_sensor

    def needs_service(self):
        return sum(self.wear_sensor) >= 3.0