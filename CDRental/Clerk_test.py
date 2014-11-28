import unittest
from clerk import Clerk
from customer import Customer

class ClerkTest(unittest.TestCase):
    def test_bank_is_initially_empty(self):
      bank = Bank()
      self.assertEqual({}, bank.accounts)
      self.assertEqual(len(bank.accounts), 0)
	
    def test_clerk_object_can_checkout(self):
      clerk = Clerk("001", "01")
      self.assertEqual(clerk.customer_id, "001")
      self.assertEqual(clerk.cd_id, "01")
