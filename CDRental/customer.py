class Customer(object):
    '''def __init__(self, customer_id, customer_name, rented):
      self.accounts = {}
      self.accounts[customer_id] = [customer_name,rented]'''
    def __init__(self, customer_id, customer_name, cd_title):
      self.accounts = {}
      self.accounts[customer_id] = [customer_name,cd_title]

    def add_customer(self, customer_id, customer_name):
      self.customer_id = customer_id
      self.customer_name = customer_name