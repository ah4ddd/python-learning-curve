from random import choice

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
            print(name, "WIN:" if pick in info["lucky"] else "LOSE:", pick)
            return

        for n, info in self.categories.items():
            pick = choice(info["values"])
            print(n, "WIN:" if pick in info["lucky"] else "LOSE:", pick)
        print()

    def until_win(self, name=None):
        if name:
            info = self.categories[name]
            tries = 0
            while True:
                tries += 1
                if choice(info["values"]) in info["lucky"]:
                    print(name, "won after", tries, "tries")
                    break
            return

        for n, info in self.categories.items():
            tries = 0
            while True:
                tries += 1
                if choice(info["values"]) in info["lucky"]:
                    print(n, "won after", tries, "tries")
                    break

game = Lottery()

# play just words
game.play("words")

# play just numbers
game.play("numbers")

# play all
game.play()

# until word wins
game.until_win("words")

# until number wins
game.until_win("numbers")

# until everything wins
game.until_win()

