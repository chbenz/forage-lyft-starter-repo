import unittest
import sys
from datetime import datetime

sys.path.append('..')
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

mileage_0 = 0
mileage_1 = 1
mileage_30k = 30000
mileage_60k = 60000
mileage_30k1 = 30001
mileage_60k1 = 60001

class TestCapuletEngine(unittest.TestCase):
    def test_need_no_service(self):
        engine0 = CapuletEngine(mileage_1, mileage_0)
        engine1 = CapuletEngine(mileage_30k, mileage_0)
        
        self.assertFalse(engine0.needs_service())
        self.assertFalse(engine1.needs_service())
    
    def test_need_service(self):
        engine = CapuletEngine(mileage_30k1, mileage_0)
        
        self.assertTrue(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_need_no_service(self):
        engine0 = WilloughbyEngine(mileage_1, mileage_0)
        engine1 = WilloughbyEngine(mileage_60k, mileage_0)
        
        self.assertFalse(engine0.needs_service())
        self.assertFalse(engine1.needs_service())
    
    def test_need_service(self):
        engine = WilloughbyEngine(mileage_60k1, mileage_0)

        self.assertTrue(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_need_no_service(self):
        engine = SternmanEngine(False)
        
        self.assertFalse(engine.needs_service())
    
    def test_need_service(self):
        engine = SternmanEngine(True)

        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()