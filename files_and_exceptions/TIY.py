from pathlib import Path
import json

path = Path('favnumb.json')

def get_new_number(path):
    while True:
        try:
            numb = int(input("What is your favorite number? "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    path.write_text(json.dumps(numb))
    return numb

def stored_number(path):
    if path.exists():
        return json.loads(path.read_text())
    return None

def fav_number():
    numb = stored_number(path)
    if numb is not None:
        print(f"I know your favorite number! It's {numb}.")
    else:
        numb = get_new_number(path)
        print(f"I'll remember your favorite number when you come back: {numb}.")

fav_number()
