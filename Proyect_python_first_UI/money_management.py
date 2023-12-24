import time
from transactions import Transaction
 
def add_money_to_account (data_for_table_finance):
 money_to_be_added_on_account = str()
 category_of_the_transaction = input("category")
 transaction_type = "Deposit"
 new_transaction_made_on_account = Transaction(money_to_be_added_on_account,category_of_the_transaction,transaction_type)
 data_for_table_finance.append(new_transaction_made_on_account)
 return data_for_table_finance