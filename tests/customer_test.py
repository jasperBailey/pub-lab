from src.customer import *
from src.pub import *
from src.drink import *
import unittest

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Caley Sample Room", 1000.00)
        self.tennents = Drink("Tennent's", 3.80, 3)
        self.guinness = Drink("Guinness", 5.20, 2)
        self.customer = Customer("Sarah", 10.00, 21)

    def test_has_name(self):
        self.assertEqual("Sarah", self.customer.name)

    def test_has_wallet(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_deduct_from_wallet(self):
        self.customer.deduct_from_wallet(4.40)
        self.assertEqual(5.60, self.customer.wallet)

    def test_request_serve_drink(self):
        self.pub.add_drink(self.tennents)
        self.pub.request_serve_drink(self.customer, "Tennent's")
        self.assertEqual(6.20, self.customer.wallet)
        self.assertEqual(1003.80, self.pub.till)

    def test_request_serve_drink_not_found(self):
        self.pub.request_serve_drink(self.customer, "Tennent's")
        self.assertEqual(10.00, self.customer.wallet)
        self.assertEqual(1000.00, self.pub.till)

    def test_request_serve_drink_insufficient_funds(self):
        customer = Customer("Jasper", 1.00, 24)
        self.pub.add_drink(self.tennents)
        self.pub.request_serve_drink(customer, "Tennent's")
        self.assertEqual(1.00, customer.wallet)
        self.assertEqual(1000.00, self.pub.till)

    def test_check_money(self):
        expected = True
        actual = self.customer.check_money(.50)
        self.assertEqual(expected, actual)

    def test_check_money_insufficient_funds(self):
        expected = False
        actual = self.customer.check_money(100)
        self.assertEqual(expected, actual)

    def test_request_serve_drink_underage(self):
        customer = Customer("Jasper", 10.00, 16)
        self.pub.add_drink(self.tennents)
        self.pub.request_serve_drink(customer, "Tennent's")
        self.assertEqual(10.00, customer.wallet)
        self.assertEqual(1000.00, self.pub.till)

    def test_drink_drink(self):
        self.customer.drink_drink(self.guinness)
        self.assertEqual(2, self.customer.drunkeness)

    def test_request_serve_drink_too_drunk(self):
        customer = Customer("Jasper", 50.00, 18)
        self.pub.add_drink(self.tennents)
        for i in range(7):
            self.pub.request_serve_drink(customer, "Tennent's")
        self.assertAlmostEqual(27.20, customer.wallet, 2)
        self.assertAlmostEqual(1022.80, self.pub.till, 2)
        self.assertEqual(18, customer.drunkeness)