class Car:
    owner = "Ahad"
    cars = 0
    def __init__(self, maker, model, year):
        self.__maker = maker
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0
        Car.cars += 1

    def get_descriptive_name(self):
        long_name = f"{self.__year} {self.__maker} {self.__model}"
        return long_name.title()

    @property
    def odometer(self):
        return self.__odometer_reading

    @odometer.setter
    def odometer(self,milage):
        self.__odometer_reading += milage

    @odometer.deleter
    def odometer(self):
        self.__odometer_reading = 0

    def set_odometer(self, milage):
        self.__odometer_reading += milage

    def read_odometer(self):
        print(f"{self.__maker.title()} {self.__model.title()} has {self.__odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.__odometer_reading:
            self.__odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.__odometer_reading += miles

    def refuel(self,fuel):
        self.fuel = fuel
        print(f"Filling... Your {self.__maker.title()} {self.__model.title()} has now {self.fuel} litres of fuel.")

    def get_mileage_status(self):
        if self.__odometer_reading < 10000:
            print(f"{self.get_descriptive_name()} is basically new!")
        elif self.__odometer_reading < 50000:
            print(f"{self.get_descriptive_name()} is well-driven.")
        else:
            print(f"{self.get_descriptive_name()} is a veteran on the road.")

    def drive(self, distance):
        self.__odometer_reading += distance
        print(f"Drove {distance} miles. Total mileage: {self.__odometer_reading} miles")

    def get_price(self, price):
        self.price = price
        print(f"Your {self.get_descriptive_name()} cost at {self.price}$")
