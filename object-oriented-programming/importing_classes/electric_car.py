from car import Car
from battery import Battery

class ElectricCar(Car):
    def __init__(self, maker, model, year):
        super().__init__(maker, model, year)
        self.battery = Battery()

    def charge(self):
        print(f"Charging the {self.maker} {self.model}...")
