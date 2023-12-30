import json,verifications
import PySimpleGUI as sg

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
    
 
def create_new_category():
 layout = [[sg.Text("Insert the name of the category"), sg.Input("Type the name of your category", key = "name_of_the_category")],
        [sg.Button("Agregar")],
    ]
 window = sg.Window("New category", layout)

 while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Agregar":
            window.close()
            return [values["name_of_the_category"]]

 window.close()


def list_of_categories_initialize(data_for_table_with_the_categories):
   if data_for_table_with_the_categories != [] :    
     for i in range (0, len(data_for_table_with_the_categories)):
        lista_categories_to_return = data_for_table_with_the_categories[i].category_of_the_transaction
     return lista_categories_to_return


def window_request_user_transaction_information(list_of_categories):
  names = list_of_categories 
  lst = sg.Combo(names,key='-COMBO-')
  layout = [[lst],
        [sg.Button("Aceptar")],
    ]

    # Crear la ventana
  window = sg.Window("New employee", layout)

  while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Aceptar":
            window.close()
            return [values["first_name"], values["role"]]

  window.close()

def add_money_to_account (data_for_table_finance):
 money_to_be_added_on_account = verifications.money_to_be_added_input()
 category_of_the_transaction = input("category")
 transaction_type = "Deposit"
 new_transaction_made_on_account = Transaction(money_to_be_added_on_account,category_of_the_transaction,transaction_type)
 data_for_table_finance.append(new_transaction_made_on_account)
 return data_for_table_finance
