from src.pub import *
from src.drink import *
import unittest

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Caley Sample Room", 1000.00)
        self.tennents = Drink("Tennent's", 3.80)

    def test_has_name(self):
        self.assertEqual("The Caley Sample Room", self.pub.name)

    def test_has_till(self):
        self.assertEqual(1000.00, self.pub.till)

    def test_add_drink(self):
        self.pub.add_drink(self.tennents)
        self.assertEqual(1, len(self.pub.get_drinks()))

    def test_add_money_to_till(self):
        self.pub.add_money_to_till(5.80)
        self.assertEqual(1005.80, self.pub.till)

    def test_find_drink_by_name(self):
        self.pub.add_drink(self.tennents)
        expected = self.tennents
        actual = self.pub.find_drink_by_name("Tennent's")
        self.assertEqual(expected, actual)

    def test_find_drink_by_name_not_found(self):
        expected = None
        actual = self.pub.find_drink_by_name("Tennent's")
        self.assertEqual(expected, actual)