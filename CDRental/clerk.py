from cd import cd
from customer import Customer

class Clerk(object):
    def __init__(self):
      self.information = {}

    '''def __init__(self, customer, cd):
      self.customer_id = customer_id
      self.cd_id = cd_id '''
    
    def checkout(self, customer, cd):
      self.info