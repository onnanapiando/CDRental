import unittest
from cdList import CDList

class CDListTest(unittest.TestCase):
    def test_CDList_is_initially_empty(self):
      cdlist = CDList("i am the info", "01","Hunger Games")
      self.assertEqual(["01", "Hunger Games"], cdlist.list["i am the info"])
      self.assertEqual(len(cdlist.list), 1)     

    def test_add_cd(self):
      cdlist = CDList("i am the info", "01","Hunger Games")
      cd_1 = CDList("i am the info", "01","Hunger Games")
      cdlist.add_cd("i am the info")
      #cdlist.add_cd("i am the info", "02","Catching Fire")
      self.assertEqual(len(cdlist.list), 2)