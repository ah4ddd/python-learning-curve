class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}: Woof!")

    def play_with(self, other_dog):
        print(f"{self.name} is playing with {other_dog.name}!")

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
dog3 = Dog("Luna", 2)

dog1.bark()

dog2.bark()

dog1.play_with(dog2)

dog3.play_with(dog1)

Dog.play_with(dog1, dog2)
