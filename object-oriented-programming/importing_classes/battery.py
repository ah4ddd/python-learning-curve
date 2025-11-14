class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This battery is {self.battery_size}-kWh")

    def get_range(self):
        if self.battery_size == 75:
            range_miles = 260
        else:
            range_miles = 315
        print(f"This car can go about {range_miles} miles on a full charge")
