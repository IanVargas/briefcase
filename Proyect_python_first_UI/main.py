
import PySimpleGUI as sg
import menu


def open_new_window():
    layout = [[sg.Image('Proyect_python_first_UI/images/logo.png',size = (800,500))],[sg.Button("Start")] ]

    window = sg.Window("Your finance!", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Start" : 
           window.close()
           menu.entry_point()
           


    window.close()


open_new_window()  