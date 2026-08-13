import PySimpleGUI as sg


def show_retry_popup(error_message):
    layout = [
        [sg.Text(f"Error: {error_message}", font=("Helvetica", 10))],
        [sg.Button("Retry", key="-RETRY-", button_color=("black", "white"), size=(10, 1))]
    ]

    window = sg.Window("Error", layout, element_justification="center", modal=True)
    while True:
        event, _ = window.read()
        if event in (sg.WINDOW_CLOSED, "-RETRY-"):
            break
    window.close()


def validate_name(name):
    if not name:
        show_retry_popup("Name cannot be empty.")
        return False
    if len(name) < 5:
        show_retry_popup("Name must be at least 5 characters long.")
        return False
    if not name.replace(" ", "").isalpha():
        show_retry_popup("Name can only contain letters and spaces.")
        return False
    return True


def validate_contact_number(contact_number):
    if not contact_number:
        show_retry_popup("Contact number cannot be empty.")
        return False
    if not contact_number.isdigit():
        show_retry_popup("Contact number must contain only digits.")
        return False
    if len(contact_number) != 11:
        show_retry_popup("Contact number must be exactly 11 digits long.")
        return False
    return True


def validate_address(address):
    if not address:
        show_retry_popup("Address cannot be empty.")
        return False
    if len(address) < 10:
        show_retry_popup("Address must be at least 10 characters long.")
        return False
    return True