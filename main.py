## Electronic Retailing System
# Cedric Capuno
# Kellie De Guzman
# Francis Tagunicar

import PySimpleGUI as sg
from pathlib import Path

# Define the window's contents
layout = [[sg.Text("What's your order?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text("What's your name?")],
          [sg.Input(key='-INPUT2-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Electronic Retailing System', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    filename = values['-INPUT2-']
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    try:
        with open(filename, 'w') as f:
            content = f.write(values['-INPUT-'])
    except FileNotFoundError:
        window['-OUTPUT-'].update(values['-OUTPUT-'])
    window['-OUTPUT-'].update("Thanks for ordering!")

# Finish up by removing from the screen
window.close()
