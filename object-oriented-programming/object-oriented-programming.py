class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0

    def accelerate(self):
        self.speed += 10
