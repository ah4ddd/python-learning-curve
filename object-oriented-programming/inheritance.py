class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Animal __init__ called for {name}")

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
        print(f"Dog __init__ called for {name}")

    def bark(self):
        print(f"{self.name} says: Woof!")

my_dog = Dog("Buddy", 3, "Golden Retriever")

my_dog.eat()

print(my_dog.name)
print(my_dog.age)
print(my_dog.breed)
