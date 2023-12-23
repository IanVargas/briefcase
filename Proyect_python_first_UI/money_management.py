import time

class MoneyFunds: 
 bank_account_id : int
 total_money_on_account : 0.00

 def __init__(self,bank_account_id,total_money_on_account) :
  self.total_money_on_account = total_money_on_account
  self.bank_account_id = bank_account_id
 
 def add_money_to_account_object(self,add_money):
    self.total_money_on_account += add_money
    return self.total_money_on_account 




def add_money_to_account (data_for_table_finance,money_mnanagement_object_funds):
 amount_of_the_transaction = money_to_be_added_verification()
 total_money_on_the_account = money_mnanagement_object_funds.add_money_to_account_object(money_to_be_added_on_account) 
 category_of_the_transaction = input("category")
 transaction_type = "Deposit"
 new_transaction_register = [{
   "Amount of the transaction" : amount_of_the_transaction, 
   "Category" : category_of_the_transaction, 
   "Type " : transaction_type}]
 
 data_for_table_finance.append(new_transaction_register)
 #return data_for_table_finance
 
 
 

def money_to_be_added_verification():
  ammount_of_money = -1
  continue_to_next_phase = True
  while  continue_to_next_phase :
       try:
        ammount_of_money = float(input("How much money are you adding?"))
       except ValueError:
        print("Wrong Input!! please input a number")
       if ammount_of_money <= -1:
         print ("You can't add negative numbers")
       elif ammount_of_money == 0:
         print("nothing will be added to the account, Thanks!")
         continue_to_next_phase = False  
         time.sleep(1)
         return 
       else: 
         continue_to_next_phase = False  
  return ammount_of_money



#def withdraw_money_from_account()
#money = MoneyFunds(0,0)
#test = [] 
#add_money_to_account(test,money)