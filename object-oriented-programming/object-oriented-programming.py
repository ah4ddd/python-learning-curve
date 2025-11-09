class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")
    def hbd(self):
        print(f"yay! {self.name} has turned {self.age+1} years old.")

my_dog = Dog("Roby", 6)
your_dog = Dog("Nina", 4)

print(f"My dog's name is {my_dog.name}.")
print(f"My {my_dog.name} is {my_dog.age} years old.")
print(f"My {my_dog.name}'s birthday is coming soon..")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your {your_dog.name} is {your_dog.age} years old.\n")
your_dog.sit()

my_dog.roll_over()
my_dog.hbd()
