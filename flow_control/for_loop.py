# Ultimate Adventure Game
# A simple text-based adventure game demonstrating for loops, nested loops, and control flow.

import random

# Player setup
player_name = input("Enter your adventurer's name: ").strip()
points = 0

print(f"\nWelcome, {player_name}! Your quest begins...\n")

# Dungeon has 3 rooms
for room in range(1, 4):
    print(f"--- Entering Room {room} ---")
    monsters = ["Goblin", "Orc", "Troll"]

    # Nested loop: fight monsters
    for monster in monsters:
        action = input(f"A {monster} appears! (fight/run/quit): ").lower().strip()

        if action == "run":
            print(f"You skipped the {monster}.")
            continue  # skip this monster

        elif action == "quit":
            print("You fled the dungeon! Game over.")
            break  # break out of monster loop

        elif action == "fight":
            # Randomly decide outcome
            if random.randint(0, 1) == 1:
                print(f"You defeated the {monster}! 💪")
                points += 10
            else:
                print(f"The {monster} hit you! You lose 5 points 😢")
                points -= 5
        else:
            print("Invalid action. The monster attacks! You lose 5 points.")
            points -= 5

    else:
        # Else runs if we didn't break (quit)
        print(f"Room {room} cleared! ✅\n")
        continue  # move to next room

    break  # if break happened in inner loop (quit), stop dungeon

else:
    print("Congratulations! You cleared all rooms of the dungeon! 🏆")

print(f"\n{player_name}, your total points: {points}")
print("Thanks for playing the Ultimate Adventure Game!")
