import PySimpleGUI as sg
import transactions,verifications,messages,os

def entry_point():
   if os.path.exists("user_transactions.json"): 
    data_for_table_finance = transactions.Transaction.import_json_to_object()
    check_up = verifications.verify_table_is_none(data_for_table_finance)
    if check_up:
     list_of_categories = transactions.list_of_categories_initialize(data_for_table_finance)
     #data_for_table_finance = transactions.Transaction.object_to_list(data_for_table_finance)
     main_menu_program(data_for_table_finance,list_of_categories)
    else:
       list_of_categories = []
       data_for_table_finance = []
       main_menu_program(data_for_table_finance,list_of_categories)
   else:
       list_of_categories = []
       data_for_table_finance = []
       main_menu_program(data_for_table_finance,list_of_categories)

def main_menu_program(data_for_table_finance,list_of_categories):  
    headers = ["Amount", "Category","Type of transaction"]
    layout = [ [sg.Table(transactions.Transaction.object_to_list(data_for_table_finance), headers, expand_x=True,expand_y=True, key="Transaction-data")],
               [sg.Button("Add a transaction"),sg.Button("Add New Category"),sg.Button("Export data"),sg.Button("Delete record data")] ]
    window = sg.Window("Your finance!", layout,size = (600 ,600))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Add a transaction" : 
         if list_of_categories == []:
            messages.no_category_on_the_system()
         else:
          window["Transaction-data"].update(transactions.Transaction.object_to_list(process_a_transaction(data_for_table_finance,list_of_categories)))
        elif event == "Add New Category" :
          new_category =  transactions.create_new_category()
          list_of_categories.append(new_category)
        elif event == "Export data":
           export_data_to_json(data_for_table_finance)
        elif event == "Delete record data":
           delete_json_file_from_system()
           entry_point()
           window.close()          

    window.close()

def export_data_to_json(data_for_table_finance):
    
 try:   
     if data_for_table_finance != []:
        transactions.Transaction.export_object_to_json(data_for_table_finance)
        messages.file_exported_successfully()
     else:
        messages.no_category_on_the_system
        main_menu_program(data_for_table_finance)
 except ValueError:
     return 
 
def  delete_json_file_from_system():
   if os.path.exists("user_transactions.json"):
        os.remove("user_transactions.json")
        messages.file_deleted_successfully()
   else:
      messages.no_file_on_the_system()     

def process_a_transaction(data_for_table_finance,list_of_categories):
 data_for_table_finance.append(transactions.window_request_user_transaction_information(list_of_categories))
 return data_for_table_finance    