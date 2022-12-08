from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear_sensor):
        self.wear_sensor = wear_sensor

    def needs_service(self):
        return any(i >= 0.9 for i in self.wear_sensor)