from pathlib import Path
import json

path = Path('username.json')

def get_new_user(path):
    """
    takes new user input
    """
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def stored_user(path):
    """
    runs if username already in file
    """
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def greet():
    """
    greet user by name
    """
    username = stored_user(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_user(path)
        print(f"we'll remembe you when you comeback, {username}!")

greet()
