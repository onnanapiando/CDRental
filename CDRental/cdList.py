from cd import CD

class CDList(object):
    def __init__(self):
      self.list = {}
      #self.list[cd_info] = [cd_id, cd_title]

    def add_cd(self, cd):
      self.list[cd.cd_id] = cd.cd_name

    def get_cd_id(self, cd_name):
      return self.list.get(cd_name)