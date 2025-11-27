class Car:
    owner = "Ahad"
    cars = 0
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        self._odometer_reading = 0
        Car.cars += 1

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.maker} {self.model}"
        return long_name.title()

    def set_odometer(self, milage):
        self._odometer_reading += milage

    def read_odometer(self):
        print(f"{self.maker.title()} {self.model.title()} has {self._odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self._odometer_reading:
            self._odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self._odometer_reading += miles

    def refuel(self,fuel):
        self.fuel = fuel
        print(f"Filling... Your {self.maker.title()} {self.model.title()} has now {self.fuel} litres of fuel.")

    def get_mileage_status(self):
        if self._odometer_reading < 10000:
            print(f"{self.get_descriptive_name()} is basically new!")
        elif self._odometer_reading < 50000:
            print(f"{self.get_descriptive_name()} is well-driven.")
        else:
            print(f"{self.get_descriptive_name()} is a veteran on the road.")

    def drive(self, distance):
        self._odometer_reading += distance
        print(f"Drove {distance} miles. Total mileage: {self._odometer_reading} miles")

    def get_price(self, price):
        self.price = price
        print(f"Your {self.get_descriptive_name()} cost at {self.price}$")




