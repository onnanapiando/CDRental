class CDRental(object):
    def __init__(self, customer_id, cd_id, rental_fee):
      self.customer_id = customer_id
      self.cd_id = cd_id
      self.rental_fee = rental_fee 

    def existing_customer_id(self, customer_id):
       self.customer_id = customer_id
       customer_id != 'None'
      
    def existing_cd_id(self, cd_id):
       self.cd_id = cd_id
       cd_id != 'None'

    def cd_rental_limit(self, customer_id, cd_id):
       self.customer_id = customer_id
       cd_id != 'None'