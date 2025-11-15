class Privileges:
    def __init__(self):
        self.privileges = [
            "Can Post",
            "Can ban users",
            "Can delete post",
            "Can Manage messages",
            "Can managage users",
            "Can access admin panel"
            ]
    def show_privileges(self):
        print(f"{"-"*5}Admin Priviledges{"-"*5}\n")
        for admin in self.privileges:
            print(f"{admin}")
