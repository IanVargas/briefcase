import PySimpleGUI as sg
import money_management,transactions,verifications,messages

def entry_point():
    data_for_table_finance = transactions.Transaction.import_json_to_object()
    check_up = verifications.verify_table_is_none(data_for_table_finance)
    if not check_up:
     list_of_categories = money_management.list_of_categories_initialize(data_for_table_finance)
     data_for_table_finance = transactions.Transaction.object_to_list(data_for_table_finance)
     main_menu_program(data_for_table_finance,list_of_categories)
     print(data_for_table_finance)
    else:
       list_of_categories = []
       data_for_table_finance = []
       print("vacia")
       main_menu_program(data_for_table_finance,list_of_categories)

def main_menu_program(data_for_table_finance,list_of_categories):
    
    headers = ["Title", "Amount","Category"]

    #data_for_table_finance = transactions.Transaction.object_to_list(data_for_table_finance)
    layout = [ [sg.Table(data_for_table_finance, headers, expand_x=True,expand_y=True, key="Transaction-data")],
               [sg.Button("add"),sg.Button("Add New Category")] ]
    

    # Crear la ventana 
    window = sg.Window("Your finance!", layout,size = (500 ,500))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "add" : 
          if list_of_categories == []:
             messages.no_category_on_the_system()
          else: 
              data_for_table_finance.append(transactions.window_request_user_transaction_information(list_of_categories))
              window["Transaction-data"].update(transactions.Transaction.object_to_list(data_for_table_finance))  
        elif event == "Add New Category" :
          new_category =  transactions.create_new_category()
          list_of_categories.append(new_category)
           

    window.close()

entry_point()