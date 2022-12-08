from abc import ABC

from serviceable import Serviceable

class Battery(Serviceable, ABC):
    def needs_service():
        pass