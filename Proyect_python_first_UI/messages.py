import PySimpleGUI as sg

def error_wrong_value_window():
  ch = sg.popup_no_buttons("Wrong Value Used, please Input just numbers",title="wrong Value",auto_close=True)
  if ch=="OK":
    sg.WINDOW_CLOSED

def no_category_on_the_system():
 ch = sg.popup_ok("There's no categories on the system, please add a category",title="wrong Value",auto_close=True)
 if ch=="OK":
    sg.WINDOW_CLOSED

