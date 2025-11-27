from car import Car

class Subaru(Car):
     def __init__(self,make, model, year):
         super().__init__(make, model, year)

     def get_subaru(self):
         print(f"{self.get_descriptive_name()} also owned by {Car.owner}")
