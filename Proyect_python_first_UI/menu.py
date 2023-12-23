import PySimpleGUI as sg
import money_management

def entry_point():
    data_for_table_finance = [
       
 ["hola","100","food"] ,["100"] , ["food"]
    ]
    money_mnanagement_object_funds = money_management.MoneyFunds(0,0)
    main_menu_program(data_for_table_finance, money_mnanagement_object_funds)

def main_menu_program(data_for_table_finance,money_mnanagement_object_funds):
    headers = ["Title", "Amount","Category"]
         
    # Declarar los elementos
    
#   tbl1 =  sg.Table(values=rows, headings=toprow,
#     auto_size_columns=True,
#     display_row_numbers=False,
#     justification='center', key='-TABLE-',
#     selected_row_colors='red on yellow',
#     enable_events=True,
#     expand_x=True,
#     expand_y=True,
#     enable_click_events=True

    layout = [ [sg.Table(data_for_table_finance, headers, expand_x=True,expand_y=True,)],
               [sg.Button("add"),sg.Button("New Category")] ]
    

    # Crear la ventana 
    window = sg.Window("Your finance!", layout,size = (500 ,500))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "add" : 
          data_for_table_finance = money_management.add_money_to_account(data_for_table_finance,money_mnanagement_object_funds)
        #elif event == ""
        if '+CLICKED+' in event :
         sg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))     

    window.close()


