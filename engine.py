from abc import ABC

from serviceable import Serviceable

class Engine(Serviceable, ABC):
    def needs_service():
        pass