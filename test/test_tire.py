import unittest
import sys

sys.path.append('..')
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

tire_ok = [0.5, 0.5, 0.5, 0.5]
carrigan_no = [0.5, 0.9, 0.5, 0.5]
octoprime_no = [0.8, 0.8, 0.8, 0.8]

class TestCarriganTire(unittest.TestCase):
    def test_need_no_service(self):
        carrigan = CarriganTire(tire_ok)

        self.assertFalse(carrigan.needs_service())

    def test_need_service(self):
        carrigan = CarriganTire(carrigan_no)

        self.assertTrue(carrigan.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_need_no_service(self):
        octoprime = OctoprimeTire(tire_ok)

        self.assertFalse(octoprime.needs_service())

    def test_need_service(self):
        octoprime = OctoprimeTire(octoprime_no)

        self.assertTrue(octoprime.needs_service())

if __name__ == '__main__':
    unittest.main()