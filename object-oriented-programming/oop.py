class User:
    def __setattr__(self, name, value):
        if isinstance(value, str):
            value = value.strip()

        if name == "age":
            value = int(value)

        super().__setattr__(name, value)

u = User()
u.name = "    Ahad    "
u.age = "25"
print(u.name)
print(u.age)
