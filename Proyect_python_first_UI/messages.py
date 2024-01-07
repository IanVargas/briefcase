import PySimpleGUI as sg


def error_wrong_value_window():
  ch = sg.popup_no_buttons("Wrong Value Used, please Input just numbers",title="wrong Value",auto_close=True)
  if ch=="OK":
    sg.WINDOW_CLOSED

def need_to_select_a_transaction_type():
  ch = sg.popup_no_buttons("You need to select a transaction type!",title="wrong Value",auto_close=True)
  if ch=="OK":
    sg.WINDOW_CLOSED  

def no_category_on_the_system():
 ch = sg.popup_ok("There's no categories on the system, please add a category",title="wrong Value",auto_close=True)
 if ch=="OK":
    sg.WINDOW_CLOSED

def no_data_on_table_the_system():
 ch = sg.popup_ok("There's no information to export",title="wrong Value",auto_close=True)
 if ch=="OK":
    sg.WINDOW_CLOSED    

def file_exported_successfully():
 ch = sg.popup_no_buttons("File Created Successfully",title="wrong Value",auto_close=True)
 if ch=="OK":
    sg.WINDOW_CLOSED    

def file_deleted_successfully():
 ch = sg.popup_no_buttons("File Deleted Successfully",title="wrong Value",auto_close=True)
 if ch=="OK":
    sg.WINDOW_CLOSED    

def no_file_on_the_system():
 ch = sg.popup_no_buttons("File Doesn't exist",title="wrong Value",auto_close=True)
 if ch=="OK":
    sg.WINDOW_CLOSED    
 