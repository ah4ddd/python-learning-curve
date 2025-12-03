class Human:
    def __setattr__(self, name, value):
        if name == "age" and value < 0:
            print("Age cannot be negative. Resetting to 0.")
            value = 0
        super().__setattr__(name, value)

h = Human()
h.age = -99
print(h.age)
