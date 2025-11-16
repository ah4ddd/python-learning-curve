class Car:
    def __init__(self,fuel):
        self._fuel = fuel

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, litres):
        if litres < 0:
            print(f"fuel cant be {litres}")
        else :
            self._fuel += litres
            print(f"added {litres} to your current fuel. total fuel : {self._fuel} litres")

    @fuel.deleter
    def fuel(self):
        self._fuel = 0
        print(f"your fuel is set back to {self._fuel} litres")

car = Car(5)

print(car.fuel)
car.fuel = 15
print(car.fuel)

del car.fuel

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(2)
