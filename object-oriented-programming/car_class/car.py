class Car:
    owner = "Ahad"
    cars = 0
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer_reading = 0
        Car.cars += 1

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.maker} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"{self.maker.title()} {self.model.title()} has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def refuel(self,fuel):
        self.fuel = fuel
        print(f"Filling... Your {self.maker.title()} {self.model.title()} has now {self.fuel} litres of fuel.")

    def get_mileage_status(self):
        if self.odometer_reading < 10000:
            print(f"{self.get_descriptive_name()} is basically new!")
        elif self.odometer_reading < 50000:
            print(f"{self.get_descriptive_name()} is well-driven.")
        else:
            print(f"{self.get_descriptive_name()} is a veteran on the road.")

    def drive(self, distance):
        self.odometer_reading = self.odometer_reading + distance
        print(f"Drove {distance} miles. Total mileage: {self.odometer_reading} miles")

    def get_price(self, price):
        self.price = price
        print(f"Your {self.get_descriptive_name()} cost at {self.price}$")

class Ferrari(Car):
    def __init__(self, maker, model, year, color):
        super().__init__(maker, model, year,)
        self.color = color

    def rari_color (self):
        print(f"{Car.owner}'s {self.get_descriptive_name()} color is {self.color.title()}")

    def get_rari(self):
        print(f"{self.maker} {self.model} {self.year} owned by {Car.owner}")

class Subaru(Car):
     def __init__(self,make, model, year):
         super().__init__(make, model, year)

     def get_subaru(self):
         print(f"{self.maker} {self.model} {self.year} also owned by {Car.owner}")

class Battery:
    def __init__(self, battery_size=100):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    def __init__(self,make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        self.battery_percentage = 65

    def describe_battery(self):
        print(f"{self.get_descriptive_name()} has a {self.battery}-kwh battery")

    def refuel(self,):
        print(f"! Your {self.maker.title()} {self.model.title()} doesn't have gas tank, you have {self.battery_percentage}% battery left.")


