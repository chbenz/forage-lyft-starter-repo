from abc import ABC, abstractmethod

from serviceable import Serviceable

class Battery(Serviceable, ABC):
    def __init__(self):
        pass

    @abstractmethod
    def needs_service():
        pass