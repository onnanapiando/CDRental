import unittest 
from cdRental import CDRental

class CDRentalTest(unittest.TestCase):
    def test_cd_check_out(self):
      cd_rental = CDRental("001","01",100)
      self.assertEqual(cd_rental.customer_id, "001")
      self.assertEqual(cd_rental.cd_id, "01")
      self.assertEqual(cd_rental.rental_fee, 100)

    def test_customer_id_if_existing(self):
      cd_rental = CDRental("001","01",100)
      self.assertEqual(cd_rental.existing_customer_id(001), None)

    def test_cd_id_if_existing(self):
      cd_rental = CDRental("001","01",100)
      self.assertEqual(cd_rental.existing_cd_id(01), None)

    def test_cd_rental_limit(self):
      cd_rental = CDRental("001","01",100)
      self.assertEqual(cd_rental.customer_id, "001")
      self.assertEqual(cd_rental.cd_rental_limit_id(04), "Transaction Error")

if __name__ == '__main__':
    unittest.main()


