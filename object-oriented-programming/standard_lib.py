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
    def __init__(self, words, numbers):
        self.words = words
        self.numbers = numbers
        self.lucky_words = ("Python", "C++")
        self.lucky_numbers = (1, 10, 100)

    def word_ticket(self):
        pick = choice(self.words)
        if pick in self.lucky_words:
            print(f"Your Luck : {pick}\nYou won Free book on {pick} programming\n")
        else:
            print(f"You got {pick}\nsee you next time\n")

    def number_ticket(self):
        pick = choice(self.numbers)
        if pick in self.lucky_numbers:
            print(f"Lucky Number : {pick}\nyou won 10000$\n")
        else:
            print(f"Aw, so close : {pick}\nbetter luck next time\n")

    def until_word_win(self):
        tries = 0
        while True:
            tries += 1
            if choice(self.words) in self.lucky_words:
                print(f"Winning Word after {tries} tries\n")
                break

    def until_number_win(self):
        tries = 0
        while True:
            tries += 1
            if choice(self.numbers) in self.lucky_numbers:
                print(f"Winning Number after {tries} tries\n")
                break

lottery_word = ["Python", "Java", "JS", "C++", "Rust"]
lottery_number = (67, 70, 10, 3, 5, 6, 90, 75, 100, 1)


game = Lottery(lottery_word, lottery_number)

print("--- Lucky Words : Python, C++ ---")
print("--- Lucky Numbers : 1, 10, 100 ---\n")

game.word_ticket()
game.number_ticket()

game.until_word_win()
game.until_number_win()


