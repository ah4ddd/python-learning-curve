from car import Car

class Ferrari(Car):
    def __init__(self, maker, model, year, color):
        super().__init__(maker, model, year,)
        self.color = color

    def rari_color(self):
        print(f"{Car.owner}'s {self.get_descriptive_name()} color is {self.color.title()}")

    def get_rari(self):
        print(f"{self.get_descriptive_name()} owned by {Car.owner}")
