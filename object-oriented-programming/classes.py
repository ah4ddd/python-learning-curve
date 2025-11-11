class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0

    def gain_exp(self, amount):
        self.exp = self.exp + amount
        print(f"{self.name} gained {amount} EXP! Total: {self.exp}")

        if self.exp >= 100:
            self.level_up()

    def level_up(self):
        self.level = self.level + 1
        self.exp = 0
        print(f"🎉 {self.name} leveled up to Level {self.level}!")

    def display(self):
        print(f"{self.name} - Level {self.level} - EXP: {self.exp}/100")

player = Player("Ahad")

player.display()

player.gain_exp(30)

player.gain_exp(40)

player.gain_exp(50)

player.display()



