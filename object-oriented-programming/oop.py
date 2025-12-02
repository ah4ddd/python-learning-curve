class MyContext:
    def __enter__(self):
        print("Entering...")
        return "Ahad"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving...")

with MyContext() as name:
    print("Inside:", name)

class Door:
    def __enter__(self):
        print("Opening door")
        return "You walked in"

    def __exit__(self, *args):
        print("Closing door")

with Door() as status:
    print(status)
