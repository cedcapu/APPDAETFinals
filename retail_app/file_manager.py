def save_order(file_title: str, file_content: str) -> None:
    with open(file_title, "w", encoding="utf-8") as file:
        file.write(file_content)

    print(f"Order successfully saved to {file_title}.txt.")

def clean_filename():
    return