class CDList(object):
    def __init__(self, cd_info, cd_id, cd_title):
      self.list = {}
      self.list[self.cd_info] = [cd_id, cd_title]

    def add_cd(self, cd_info):
      self.list[self.cd_info] = [self.cd_id, self.cd_title]