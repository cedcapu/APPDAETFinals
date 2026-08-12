from pathlib import Path

def save_order(file_title: str, file_content: str) -> None:
    path = Path(file_title+".txt")
    if path.exists():
        with open(file_title+".txt", "a") as file:
            file.write(file_content)
    else:
        with open(file_title + ".txt", "w", encoding="utf-8") as file:
            file.write(file_content)

    print(f"Order successfully saved to {file_title}.txt.")

def clean_filename():
    return