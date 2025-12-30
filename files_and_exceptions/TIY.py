from pathlib import Path
import json

path = Path('favnumb.json')

def get_new_number(path):
    numb = int(input("What is your favorite number? "))
    contents = json.dumps(numb)
    path.write_text(contents)
    return numb

def stored_number(path):
    if path.exists():
        contents = path.read_text()
        numb = json.loads(contents)
        return numb
    else:
        return None

def fav_number():
    numb = stored_number(path)
    if numb:
        print(f"you already gave me your favorite number, its: {numb}!")
    else:
        numb = get_new_number(path)
        print(f"I'll remember your favorite number when you comeback: {numb}!")

fav_number()
