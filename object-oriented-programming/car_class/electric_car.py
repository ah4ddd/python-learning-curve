from car import Car
from battery import Battery

class ElectricCar(Car):
    def __init__(self,make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        self.battery_percentage = 65

    def describe_battery(self):
        print(f"{self.get_descriptive_name()} has a {self.battery}-kwh battery")

    def refuel(self,):
        print(f"! Your {self.__maker.title()} {self.__model.title()} doesn't have gas tank, you have {self.battery_percentage}% battery left.")
