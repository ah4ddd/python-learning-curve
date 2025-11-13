# Separate Battery class:
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This battery is {self.battery_size}-kWh")

    def get_range(self):
        if self.battery_size == 75:
            range_miles = 260
        elif self.battery_size == 100:
            range_miles = 315
        else:
            range_miles = 0
        print(f"This car can go about {range_miles} miles on a full charge")

class Car:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.maker} {self.model}".title()

class ElectricCar(Car):
    def __init__(self, maker, model, year):
        super().__init__(maker, model, year)
        self.battery = Battery()  # Create a Battery object!

    def charge(self):
        print(f"Charging the {self.maker} {self.model}...")

my_tesla = ElectricCar("Tesla", "Model 3", 2023)

print(my_tesla.get_descriptive_name())

my_tesla.charge()

my_tesla.battery.describe_battery()

my_tesla.battery.get_range()

class ElectricCarr(Car):
    def __init__(self, maker, model, year, battery_size=75):
        super().__init__(maker, model, year)
        self.battery = Battery(battery_size)  # Pass size

my_tesla_long_range = ElectricCarr("Tesla", "Model S", 2023, 100)
my_tesla_long_range.battery.get_range()
