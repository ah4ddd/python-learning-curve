class MyDemo:
    registry = []

    def __new__(cls, *args, **kwargs):
        print("Allocating memory for object")
        return super().__new__(cls)

    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __call__(self, x):
        return self.value * x

    def __enter__(self):
        print("Entering block")
        return self

    def __exit__(self, a, b, c):
        print("Leaving block")

    def __getitem__(self, index):
        return str(self.value)[index]

    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")

    def __init_subclass__(cls):
        MyDemo.registry.append(cls.__name__)
