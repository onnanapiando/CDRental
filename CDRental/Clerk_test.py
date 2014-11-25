import unittest
from clerk import Clerk
from customer import Customer

class ClerkTest(unittest.TestCase):
    def test_clerk_object_can_checkout(self):
      clerk = Clerk()
      customer = Customer("001", "Onna", 0)
      cd = CD("01","Titanic")
      clerk.checkout("001","01")

