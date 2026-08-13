import PySimpleGUI as sg
from datetime import datetime

from .config import (
    KEY_ADDRESS, KEY_NAME, KEY_NOTES, KEY_OK, KEY_ORDER,
    KEY_PAYMENT, KEY_PHONE, KEY_QUIT, KEY_STATUS,
    PAYMENT_METHODS, WINDOW_TITLE
)
from .file_manager import save_order
from .products import get_product_display_list

sg.theme("DarkTeal6")

# Generate bold label + input field in one row
def label_input(label: str, key: str, size=(40, 1)) -> list:
    return [[sg.Text(label, font=("Helvetica", 10, "bold"))], [sg.Input(key=key, size=size)]]

# Define the window's contents
def build_window() -> sg.Window:
    product_options = get_product_display_list()

    layout = [
        [sg.Text("Electronic Retailing Checkout", font=("Helvetica", 12, "bold"))],
        [sg.HorizontalSeparator()],

        # Prompt product selection
        [sg.Text("Select a Product:", font=("Helvetica", 10, "bold"))],
        [sg.Combo(products, default_value=products[0], key=KEY_ORDER, readonly=True, size=(35, 1))],

        # Ask for customer info
        *label_input("Full Name:", KEY_NAME),
        *label_input("Phone Number:", KEY_PHONE),
        *label_input("Delivery Address:", KEY_ADDRESS),

        # Ask for payment method
        [sg.Text("Mode of Payment:", font=("Helvetica", 10, "bold"))],
        [sg.Combo(PAYMENT_METHODS, default_value=PAYMENT_METHODS[0], key=KEY_PAYMENT, readonly=True, size=(38, 1))],

        # Ask for optional delivery notes
        [sg.Text("Delivery Notes (Optional):", font=("Helvetica", 10, "bold"))],
        [sg.Multiline(key=KEY_NOTES, size=(38, 3))],

        # Action buttons
        [sg.Text(size=(40, 1), key=KEY_STATUS, text_color="lightgreen")],
        [
            sg.Button(KEY_OK, button_color=("white", "forestgreen"), size=(10, 1)),
            sg.Button(KEY_QUIT, button_color=("white", "firebrick"), size=(10, 1)),
        ],
    ]

    return sg.Window(WINDOW_TITLE, layout, margins=(25, 25), element_justification="left")

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
                # Compile form data
                order_details = (
                    f"Timestamp: {datetime.now()}\n"
                    f"Product: {values[KEY_ORDER]}\n"
                    f"Phone: {values[KEY_PHONE]}\n"
                    f"Address: {values[KEY_ADDRESS]}\n"
                    f"Payment Method: {values[KEY_PAYMENT]}\n"
                    f"Notes: {values[KEY_NOTES].strip()}\n"
                )

                status = save_order(values[KEY_NAME], order_details)
                window[KEY_STATUS].update(status)
    finally:
        window.close()