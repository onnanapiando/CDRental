import unittest
from cd import CD

class TestAccount(unittest.TestCase):
    def test_account_object_can_be_created(self):
      cd = CD("01", "Hunger Games")
      self.assertEqual(cd.cd_id, "01")
      self.assertEqual(cd.cd_name, "Hunger Games")
    
    '''def test_account_if_existing(self):
       account = Account("001", 50)
       self.assertEqual(account.existing_account(001), None)'''

if __name__ == '__main__':
    unittest.main()


