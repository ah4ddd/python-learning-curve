class Car:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.maker} {self.model}".title()

class Motorcycle:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.maker} {self.model}".title()

class Truck:
    def __init__(self, maker, model, year):
        self.maker = maker
        self.model = model
        self.year = year
        self.capacity = 1000

    def get_descriptive_name(self):
        return f"{self.year} {self.maker} {self.model}".title()
