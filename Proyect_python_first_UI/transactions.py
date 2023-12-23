import json

class Transaction():
 amount_of_the_transaction = float
 category_of_the_transaction =str
 transaction_type = str

 def __init__(self,amount_of_the_transaction,category_of_the_transaction,transaction_type) :
  self.amount_of_the_transaction = amount_of_the_transaction
  self.category_of_the_transaction = category_of_the_transaction
  self.transaction_type = transaction_type
 
 def object_to_list(value_object_to_list):
    new_list = []
    for i in range (0 , len(value_object_to_list)):
      if value_object_to_list:
        new_list.append([str(value_object_to_list[i].amount_of_the_transaction), 
                        value_object_to_list[i].category_of_the_transaction,
                        value_object_to_list[i].transaction_type])
      else: 
        return
    return new_list   
 
 def object_to_json(value_object_to_json):
   new_json = []
   for i in range (0 , len(value_object_to_json)):
      if value_object_to_json:
        new_json.append({
          "Amount_of_the_transaction" : value_object_to_json[i].amount_of_the_transaction, 
          "Category" : value_object_to_json[i].category_of_the_transaction, 
          "Type " : value_object_to_json[i].transaction_type 
          })
      else: 
        return
   with open ("user_transactions.json",'w') as file:
     json.dump(new_json,file)   
    
 
#used for testing
"""
def read_pokemon_json_file () :  
 with open ("user_transactions.json", 'r') as file: 
  new_data_pokemon = json.load(file)
  return new_data_pokemon

"""
#Used for testing: 
#new_money_amount_on_acount_list = []
#new_money_amount_on_acount = Transaction(100,"FOOD","deposit") 
#new_money_amount_on_acount_list.append(new_money_amount_on_acount)
#to_list = Transaction.object_to_list(new_money_amount_on_acount_list) #
#print(to_list)

#lista = read_pokemon_json_file()
