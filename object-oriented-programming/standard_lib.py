from random import randint, choice

class DiceRoll:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        roll = randint(1, self.sides)
        return roll

    def roll_many_times(self, rolls = 10):
        for _ in range(rolls):
            roll = self.roll_dice()
            print(roll)
        return None

dice = DiceRoll()
ten_sided = DiceRoll(10)
twenty_sided  = DiceRoll(20)

print(dice.roll_dice())
print()
dice.roll_many_times()

print()
ten_sided.roll_many_times()

print()
twenty_sided.roll_many_times()
print()

class Lottery:
    def __init__(self):
        self.categories = {
            "words": {
                "values": ["Python", "Java", "JS", "C++", "Rust"],
                "lucky": ["Python", "C++"]
            },
            "numbers": {
                "values": [67,70,10,3,5,6,90,75,100,1],
                "lucky": [1,10,100]
            }

        }

    def play(self, name=None):
        if name:
            info = self.categories[name]
            pick = choice(info["values"])

            if pick in info["lucky"]:
                print(f"{name} pulled {pick}.\nLook at you, actually getting something right for once.")
            else:
                print(f"{name} pulled {pick}.\nSweet, I am not even disappointed. I expected this.")
            return

        for n, info in self.categories.items():
            pick = choice(info["values"])

            if pick in info["lucky"]:
                print(f"{n} hit {pick}.\nWow. Even you stumble into wins sometimes.")
            else:
                print(f"{n} got {pick}.\nClassic you. Predictably unlucky.")
        print()

    def until_win(self, name=None):
        if name:
            info = self.categories[name]
            tries = 0

            while True:
                tries += 1
                pick = choice(info["values"])
                if pick in info["lucky"]:
                    print(f"{name} won after {tries} tries.\nTook you long enough, but hey… you made it.")
                    break
            return

        for n, info in self.categories.items():
            tries = 0

            while True:
                tries += 1
                pick = choice(info["values"])
                if pick in info["lucky"]:
                    print(f"{n} won after {tries} attempts.\nI was starting to worry you'd never get there.")
                    break

game = Lottery()

print("--- Lucky Words : Python, C++ ---")
print("--- Lucky Numbers : 1, 10, 100 ---\n")

game.play("words")
game.play("numbers")

game.play()

game.until_win("words")
game.until_win("numbers")
game.until_win()



