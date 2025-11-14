class Car:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self,):
        return f"{self.year} {self.maker} {self.model}".title()

    def read_odometer(self, ran):
        self.odometer_reading = ran
        print(f"This car has {self.odometer_reading} miles on it")

    def drive(self, distance):
        self.odometer_reading += distance
        print(f"Drove {distance} miles. Total: {self.odometer_reading}")
