class Vehicle:
    """Base vehicle class."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_description(self):
        """Return a description."""
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        """Return odometer reading."""
        return self.odometer

    def update_odometer(self, mileage):
        """Update odometer, reject if rolling back."""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            raise ValueError("Cannot roll back odometer!")

class Car(Vehicle):
    """Car class, inherits from Vehicle."""

    def __init__(self, make, model, year, fuel_type="gasoline"):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def get_description(self):
        """Return car description with fuel type."""
        return f"{super().get_description()} ({self.fuel_type})"

