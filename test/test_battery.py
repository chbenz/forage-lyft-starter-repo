import unittest
import sys
from datetime import datetime

sys.path.append('..')
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

today = datetime.today().date()
years_bf1 = today.replace(year=today.year - 1)
years_bf4 = today.replace(year=today.year - 4)
years_bf5 = today.replace(year=today.year - 5)

class TestSpindlerBattery(unittest.TestCase):
    def test_need_no_service(self):
        battery = SpindlerBattery(today, years_bf1)
        
        self.assertFalse(battery.needs_service())
    
    def test_need_service(self):
        battery = SpindlerBattery(today, years_bf4)
        
        self.assertTrue(battery.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_need_no_service(self):
        battery = NubbinBattery(today, years_bf4)
        
        self.assertFalse(battery.needs_service())

    def test_need_service(self):
        battery = NubbinBattery(today, years_bf5)
        
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()