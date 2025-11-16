class Car:
    def __init__(self,fuel):
        self.fuuel = fuel

    @property
    def fuel(self):
        return self.fuuel

    @fuel.setter
    def fuel(self, litres):
        if litres < 0:
            print(f"fuel cant be {litres}")
        else :
            self.fuuel += litres
            print(f"added {litres} to your current fuel. total fuel : {self.fuuel} litres")

    @fuel.deleter
    def fuel(self):
        self.fuuel = 0
        print(f"your fuel is set back to {self.fuuel} litres")

car = Car(5)

print(car.fuel)
car.fuel = 15
print(car.fuel)

del car.fuel


