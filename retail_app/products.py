PRODUCTS = [
    {"id": "P101", "name": "Wireless Ergonomic Mouse", "price": 19.99},
    {"id": "P102", "name": "Mechanical Keyboard Yellow Switches", "price": 59.99},
    {"id": "P103", "name": "27-inch OLED Monitor", "price": 189.99},
    {"id": "P104", "name": "Fifine AM8 Ampligame Microphone", "price": 24.50},
    {"id": "P105", "name": "Loops Noise Canceling Earphones", "price": 67.00},
]

def get_product_display_list() -> list[str]:
    return [f"{p['name']} - ${p['price']:.2f}" for p in PRODUCTS]