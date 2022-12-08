import unittest
import sys
from datetime import datetime

sys.path.append('..')
from car_factory import CarFactory

'''
    Whether an engine needs service depends on mileage for capulet and willoughby,
    and warning indicator for sternman, hence last service date is irrelevant.
    In this test set, the last service date will be the same, 1 year before the
    current date for variable controls.
'''

today = datetime.today().date()
years_bf1 = today.replace(year=today.year - 1)
mileage_0 = 0
mileage_1 = 1
mileage_30k = 30000
mileage_60k = 60000
mileage_30k1 = 30001
mileage_60k1 = 60001

class TestCapuletEngine(unittest.TestCase):
    def test_calliope_need_no_service(self):
        calliope0 = CarFactory.create_calliope(today, years_bf1, mileage_1, mileage_0)
        calliope1 = CarFactory.create_calliope(today, years_bf1, mileage_30k, mileage_0)

        self.assertFalse(calliope0.needs_service())
        self.assertFalse(calliope1.needs_service())
    
    def test_thovex_need_no_service(self):
        thovex0 = CarFactory.create_thovex(today, years_bf1, mileage_1, mileage_0)
        thovex1 = CarFactory.create_thovex(today, years_bf1, mileage_30k, mileage_0)

        self.assertFalse(thovex0.needs_service())
        self.assertFalse(thovex1.needs_service())

    def test_calliope_need_service(self):
        calliope = CarFactory.create_calliope(today, years_bf1, mileage_30k1, mileage_0)

        self.assertTrue(calliope.needs_service())

    def test_thovex_need_service(self):
        thovex = CarFactory.create_thovex(today, years_bf1, mileage_30k1, mileage_0)

        self.assertTrue(thovex.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_glissade_need_no_service(self):
        glissade0 = CarFactory.create_glissade(today, years_bf1, mileage_1, mileage_0)
        glissade1 = CarFactory.create_glissade(today, years_bf1, mileage_60k, mileage_0)

        self.assertFalse(glissade0.needs_service())
        self.assertFalse(glissade1.needs_service())
    
    def test_rorschach_need_no_service(self):
        rorschach0 = CarFactory.create_rorschach(today, years_bf1, mileage_1, mileage_0)
        rorschach1 = CarFactory.create_rorschach(today, years_bf1, mileage_60k, mileage_0)

        self.assertFalse(rorschach0.needs_service())
        self.assertFalse(rorschach1.needs_service())

    def test_glissade_need_service(self):
        glissade = CarFactory.create_glissade(today, years_bf1, mileage_60k1, mileage_0)

        self.assertTrue(glissade.needs_service())

    def test_rorschach_need_service(self):
        rorschach = CarFactory.create_rorschach(today, years_bf1, mileage_60k1, mileage_0)

        self.assertTrue(rorschach.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_palindrome_need_no_service(self):
        palindrome = CarFactory.create_palindrome(today, years_bf1, False)

        self.assertFalse(palindrome.needs_service())

    def test_palindrome_need_service(self):
        palindrome = CarFactory.create_palindrome(today, years_bf1, True)

        self.assertTrue(palindrome.needs_service())

if __name__ == '__main__':
    unittest.main()