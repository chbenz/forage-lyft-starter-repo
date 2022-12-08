from abc import ABC

from serviceable import Serviceable

class Tire(Serviceable, ABC):
    def needs_service():
        pass