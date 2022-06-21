from tires.carrigan_tires import CarriganTires
import unittest

class CarriganTiresTest(unittest.TestCase):
    
    def test_needs_services_true(self):
        tire_wear = [0.1, 0.3, 0.2, 0.9]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())
        
    def test_needs_services_false(self):
        tire_wear = [0.1, 0.2, 0.4, 0.2]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())
        