import PySimpleGUI as sg

def error_wrong_value_window():
  ch = sg.popup_no_buttons("Wrong Value Used, please Input just numbers",title="wrong Value",auto_close=True)
  if ch=="OK":
    sg.close.window

