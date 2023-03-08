from src.drink import *
import unittest

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink = Drink("Tennent's", 3.80, 3)

    def test_has_name(self):
        self.assertEqual("Tennent's", self.drink.name)

    def test_has_price(self):
        self.assertEqual(3.80, self.drink.price)

    def test_alcohol_level(self):
        self.assertEqual(3, self.drink.alcohol_level)
