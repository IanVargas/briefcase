
import messages

def verify_table_is_none(exceptions=()):
  try:                                                                                                                                          
    return True
  except exceptions as e:
    return False

def money_to_be_added_input(amount_of_the_transaction):
 amount_of_money_to_be_added = None
 verification = True
 while  verification:
      try:
         amount_of_money_to_be_added = float(amount_of_the_transaction)
         verification = False
         return verification
      except ValueError:
        verification = True
        return verification  







