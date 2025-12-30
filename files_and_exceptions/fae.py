from pathlib import Path
import json

path = Path("user_data.json")

def get_new_user(path):
    """
    Collect new user information and store it.
    """
    name = input("What is your name? ")
    age = input("How old are you? ")
    city = input("Which city do you live in? ")

    user_data = {
        "name": name,
        "age": age,
        "city": city
    }

    path.write_text(json.dumps(user_data))
    return user_data

def stored_user(path):
    """
    Return stored user data if it exists.
    """
    if path.exists():
        return json.loads(path.read_text())
    return None

def greet_user():
    """
    Greet user and verify identity.
    """
    user = stored_user(path)

    if user is not None:
        correct = input(f"Is your name {user['name']}? (yes/no): ").lower()

        if correct == "yes":
            print("\nWelcome back!")
            print("Here’s what I remember about you:")
            print(f"Name: {user['name']}")
            print(f"Age: {user['age']}")
            print(f"City: {user['city']}")
        else:
            print("\nOkay, let's update your information.")
            user = get_new_user(path)
            print("\nGot it. I’ll remember this about you:")
            print(f"Name: {user['name']}")
            print(f"Age: {user['age']}")
            print(f"City: {user['city']}")
    else:
        user = get_new_user(path)
        print("\nNice to meet you!")
        print("I’ll remember this about you:")
        print(f"Name: {user['name']}")
        print(f"Age: {user['age']}")
        print(f"City: {user['city']}")

greet_user()
