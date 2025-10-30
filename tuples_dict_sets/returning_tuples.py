import random

def roll_dice(num_rolls):

    rolls = []

    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        rolls.append(roll)
    roll = rolls
    total = sum(rolls)
    average = total / num_rolls
    highest = max(rolls)
    lowest = min(rolls)

    return roll, total, average, highest, lowest

num = 10
roll, total, avg, high, low = roll_dice(num)

print(f"All dices : {roll}")
print(f"🎲 Rolled {num} times:")
print(f"Total: {total}")
print(f"Average: {avg:.2f}")
print(f"Highest: {high}")
print(f"Lowest: {low}")
