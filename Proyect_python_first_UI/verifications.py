
import messages

def verify_table_is_none(exceptions=()):
  try:                                                                                                                                          
    return True
  except exceptions as e:
    return False

def money_to_be_added_input():
 amount_of_money_to_be_added = None
 verification = True
 while  verification:
      try:
        amount_of_money_to_be_added  = float(input("What's the amount of the transaction"))
        verification = False
      except ValueError:
        messages.error_wrong_value_window()
      
 return amount_of_money_to_be_added  






value = money_to_be_added_input()

