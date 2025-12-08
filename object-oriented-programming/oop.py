from user import user


class User:
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1

    def greeting(self):               # instance
        return f"Hi {self.name}"

    @classmethod
    def total_users(cls):             # class
        return cls.count

    @staticmethod
    def upper(text):                  # static
        return text.upper()

u = User ("ahad")

print(u.name)

print(User.greeting(u).title())
print(User.total_users())
print(User.upper("coco"))
