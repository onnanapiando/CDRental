import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):
    def test_customer_object_can_be_created(self):
      customer = Customer("001", "Juan")
      self.assertEqual(customer.customer_id, "001")
      self.assertEqual(customer.customer_name, "Juan")
    
    '''def test_account_if_existing(self):
       account = Account("001", 50)
       self.assertEqual(account.existing_account(001), None)'''

if __name__ == '__main__':
    unittest.main()