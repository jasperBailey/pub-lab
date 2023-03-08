from src.customer import *
from src.pub import *
from src.drink import *
import unittest

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Caley Sample Room", 1000.00)
        self.tennents = Drink("Tennent's", 3.80)
        self.guinness = Drink("Guinness", 5.20)
        self.customer = Customer("Sarah", 10.00)

    def test_has_name(self):
        self.assertEqual("Sarah", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_deduct_from_wallet(self):
        self.customer.deduct_from_wallet(4.40)
        self.assertEqual(5.60, self.customer.wallet)

    def test_buy_drink(self):
        self.pub.add_drink(self.tennents)
        self.customer.buy_drink(self.pub, "Tennent's")
        self.assertEqual(6.20, self.customer.wallet)
        self.assertEqual(1003.80, self.pub.till)

    def test_buy_drink_not_found(self):
        self.customer.buy_drink(self.pub, "Tennent's")
        self.assertEqual(10.00, self.customer.wallet)
        self.assertEqual(1000.00, self.pub.till)

    def test_buy_drink_insufficient_funds(self):
        customer = Customer("Jasper", 1.00)
        self.pub.add_drink(self.tennents)
        customer.buy_drink(self.pub, "Tennent's")
        self.assertEqual(1.00, customer.wallet)
        self.assertEqual(1000.00, self.pub.till)