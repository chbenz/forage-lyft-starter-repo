from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class Calliope(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date))

class Glissade(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(current_date, last_service_date))

class Palindrome(Car):
    def __init__(self, current_date, last_service_date, warning_light_is_on):
        super().__init__(SternmanEngine(warning_light_is_on), SpindlerBattery(current_date, last_service_date))

class Rorschach(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date))

class Thovex(Car):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super().__init__(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(current_date, last_service_date))

class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Glissade(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        return Palindrome(current_date, last_service_date, warning_light_is_on)
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Thovex(current_date, last_service_date, current_mileage, last_service_mileage)