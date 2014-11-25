import unittest
from customer import Customer

class CustomerTest(unittest.TestCase):
    def test_customer_is_initially_empty(self):
      customer = Customer("01", "Juan", "Hunger Games")
      self.assertEqual(["Juan", "Hunger Games"], customer.accounts["01"])
      self.assertEqual(len(customer.accounts), 1)

    def test_add_customer(self):
      customer = Customer("01", "Juan", "Hunger Games")
      customer_1 = customer.add_customer("01", "Juan")
      customer_2 = customer.add_customer("02", "Pedro")
      self.assertEqual(len(customer.accounts), 1)	