class Car:
    WHEELS = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print("Driving...")

    @classmethod
    def wheel_count(cls):
        return cls.WHEELS

    @staticmethod
    def honk_sound():
        return "Beep!"

    def __str__(self):
        return f"{self.brand} {self.model}"
