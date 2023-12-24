import json,verifications

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
        print("This list doesn't exist")
    return new_list   
 
 def export_object_to_json(value_object_to_json):
   new_json = []
   for i in range (0 , len(value_object_to_json)):
      if value_object_to_json:
        new_json.append({
          "amount_of_the_transaction" : value_object_to_json[i].amount_of_the_transaction, 
          "category_of_the_transaction" : value_object_to_json[i].category_of_the_transaction, 
          "transaction_type" : value_object_to_json[i].transaction_type 
          })
      else: 
        return
   with open ("user_transactions.json",'w') as file:
     json.dump(new_json,file)

 def json_to_object(json_to_convert_objetc):
   list_to_be_returned = []
   for i in range (0,len(json_to_convert_objetc)): 
     object_initializer= Transaction(json_to_convert_objetc[i]["amount_of_the_transaction"],json_to_convert_objetc[i]["category_of_the_transaction"],json_to_convert_objetc[i]["transaction_type"])
     list_to_be_returned.append(object_initializer)
   return list_to_be_returned   
 
 def import_json_to_object():
  list_of_obejcts_from_json = []
  try: 
   with open ('user_transactions.json','r') as file:
       list_of_obejcts_from_json = json.load(file)
   if list_of_obejcts_from_json != [] :     
    list_of_obejcts_from_json = Transaction.json_to_object(list_of_obejcts_from_json)        
    return list_of_obejcts_from_json
  except IOError:
   print("There's no file with that name")
    
 
#used for testing
"""
def read_pokemon_json_file () :  
 with open ("user_transactions.json", 'r') as file: 
  new_data_pokemon = json.load(file)
  return new_data_pokemon

"""
#Used for testing: 
#new_money_amount_on_acount_list = Transaction.import_json_to_object()
#new_money_amount_on_acount_list = Transaction.object_to_list(new_money_amount_on_acount_list)


"""
list_test = []
new_money_amount_on_acount_list = Transaction("100","food","deposit")
list_test.append(new_money_amount_on_acount_list)
convert = Transaction.export_object_to_json(list_test)
"""
#print(new_money_amount_on_acount_list)

