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

my_new_car = Car("Ferrari","sp3", 2021)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(45)
my_new_car.read_odometer()
my_new_car.update_odometer(30)
my_new_car.read_odometer()
my_new_car.refuel(10)
my_new_car.get_price(2000000)
my_new_car.drive(250)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_used_car.refuel(16)
my_used_car.get_mileage_status()
my_used_car.get_price(25000)

print(f"Owner : {Car.owner}")
print(f"{Car.owner} owns {Car.cars} cars, {my_new_car.get_descriptive_name()} & {my_used_car.get_descriptive_name()}")
