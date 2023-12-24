import PySimpleGUI as sg
import money_management,transactions,verifications

def entry_point():
    data_for_table_finance = transactions.Transaction.import_json_to_object()
    check_up = verifications.verify_table_is_none(data_for_table_finance)
    if not check_up:
     data_for_table_finance = transactions.Transaction.object_to_list(data_for_table_finance)
     #main_menu_program(data_for_table_finance)
     print(data_for_table_finance)
    else:
       data_for_table_finance = []
       print("vacia")
     #main_menu_program(data_for_table_finance)
"""
def main_menu_program(data_for_table_finance):
    
    headers = ["Title", "Amount","Category"]

    #data_for_table_finance = transactions.Transaction.object_to_list(data_for_table_finance)
    layout = [ [sg.Table(data_for_table_finance, headers, expand_x=True,expand_y=True,)],
               [sg.Button("add"),sg.Button("New Category")] ]
    

    # Crear la ventana 
    window = sg.Window("Your finance!", layout,size = (500 ,500))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "add" : 
          break
         #to be aded new changes
          #data_for_table_finance = money_management.add_money_to_account(data_for_table_finance,money_mnanagement_object_funds)
        #elif event == ""
        #if '+CLICKED+' in event :
         #sg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))     

    window.close()

"""

entry_point()