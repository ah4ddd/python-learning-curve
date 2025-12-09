from abc import ABC, abstractmethod

class Weapon(ABC):

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Slash!"

class Gun(Weapon):
    def attack(self):
        return "Bang!"

weapon1 = Sword()
weapon2 = Gun()

print(weapon1.attack())
print(weapon2.attack())
