import PySimpleGUI as sg

from .config import (
    KEY_NAME,
    KEY_OK,
    KEY_ORDER,
    KEY_QUIT,
    KEY_STATUS,
    WINDOW_TITLE,
)
from .file_manager import save_order

# Define the window's contents (MOVED FROM MAIN - Kellie <-- Delete later)
def build_window() -> sg.Window:
    layout = [
        [sg.Text("What's your order?")],
        [sg.Input(key=KEY_ORDER)],
        [sg.Text("What's your name?")],
        [sg.Input(key=KEY_NAME)],
        [sg.Text(size=(40, 1), key=KEY_STATUS)],
        [sg.Button(KEY_OK), sg.Button(KEY_QUIT)],
    ]
    return sg.Window(WINDOW_TITLE, layout)

# Display and interact with the Window using an Event Loop
def run() -> None:
    window = build_window()
    try:
        while True:
            event, values = window.read()
            # See if user wants to quit or window was closed
            if event in (sg.WINDOW_CLOSED, KEY_QUIT):
                break

            if event == KEY_OK:
                status = save_order(values[KEY_NAME], values[KEY_ORDER])
                window[KEY_STATUS].update(status)
    finally:
        window.close()
