import unittest
import sys
from datetime import datetime

sys.path.append('..')
from car_factory import CarFactory

'''
    Whether a battery needs service depends on length since the last service.
    In this test set, the current and last service mileage will be 0 for
    capulet and willoughby engines, warning indicator off for sternman engines.
'''

today = datetime.today().date()
years_bf1 = today.replace(year=today.year - 1)
years_bf3 = today.replace(year=today.year - 3)
years_bf5 = today.replace(year=today.year - 5)
mileage_0 = 0

class TestSpindlerBattery(unittest.TestCase):
    def test_need_no_service(self):
        calliope = CarFactory.create_calliope(today, years_bf1, mileage_0, mileage_0)
        glissade = CarFactory.create_glissade(today, years_bf1, mileage_0, mileage_0)
        palindrome = CarFactory.create_palindrome(today, years_bf1, False)

        self.assertFalse(calliope.needs_service())
        self.assertFalse(glissade.needs_service())
        self.assertFalse(palindrome.needs_service())
    
    def test_need_service(self):
        calliope = CarFactory.create_calliope(today, years_bf3, mileage_0, mileage_0)
        glissade = CarFactory.create_glissade(today, years_bf3, mileage_0, mileage_0)
        palindrome = CarFactory.create_palindrome(today, years_bf3, False)

        self.assertTrue(calliope.needs_service())
        self.assertTrue(glissade.needs_service())
        self.assertTrue(palindrome.needs_service())

class TestNubbinBattery(unittest.TestCase):
    def test_need_no_service(self):
        rorschach = CarFactory.create_rorschach(today, years_bf3, mileage_0, mileage_0)
        thovex = CarFactory.create_thovex(today, years_bf3, mileage_0, mileage_0)

        self.assertFalse(rorschach.needs_service())
        self.assertFalse(thovex.needs_service())
    
    def test_need_service(self):
        rorschach = CarFactory.create_rorschach(today, years_bf5, mileage_0, mileage_0)
        thovex = CarFactory.create_thovex(today, years_bf5, mileage_0, mileage_0)

        self.assertTrue(rorschach.needs_service())
        self.assertTrue(thovex.needs_service())

if __name__ == '__main__':
    unittest.main()