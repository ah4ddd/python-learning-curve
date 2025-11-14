class Garage:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Added {vehicle.get_descriptive_name()} to {self.name}")

    def list_vehicles(self):
        print(f"\n{self.name} contains:")
        for vehicle in self.vehicles:
            print(f"  - {vehicle.get_descriptive_name()}")
