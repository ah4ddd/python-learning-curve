from car import Car
from ferrari import Ferrari
from subaru import Subaru
from electric_car import ElectricCar

my_new_car = Ferrari("Ferrari","sp3", 2021, "red")
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
my_new_car.get_rari()
my_new_car.rari_color()

my_used_car = Subaru('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_used_car.refuel(16)
my_used_car.get_mileage_status()
my_used_car.get_price(25000)
my_used_car.get_subaru()

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.refuel()
my_tesla.get_price(80000)
my_tesla.battery.get_range()

print(f"Owner : {Car.owner}")
print(f"{Car.owner} owns {Car.cars} cars: {my_new_car.get_descriptive_name()}, {my_used_car.get_descriptive_name()} & {my_tesla.get_descriptive_name()}")
