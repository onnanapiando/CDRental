import unittest
from cdList import CDList
from cd import CD

class CustomerTest(unittest.TestCase):
    def test_cd_is_initially_empty(self):
      cdlist = CDList()
      self.assertEqual({}, cdlist.list)
      self.assertEqual(len(cdlist.list), 0)

    def test_add_cd(self):
      cdlist = CDList()
      cd_1 = CD("01", "Hunger Games")
      cd_2 = CD("02", "Catching Fire")
      cdlist.add_cd(cd_1)
      cdlist.add_cd(cd_2)
      self.assertEqual(len(cdlist.list), 2) 

    def test_get_cd_id(self):
      cdlist = CDList()
      cd_1 = CD("01", "Hunger Games")
      cdlist.add_cd(cd_1)
      self.assertEqual(cdlist.get_cd_id("01"), "Hunger Games") 