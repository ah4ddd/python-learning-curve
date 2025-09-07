
---

# **Project: Dice Roller Gambling Machine**

## **What we are building**

* A **console game** where the user rolls dice.
* User can **bet money** on the outcome.
* Dice roll is **random**.
* Player wins or loses money depending on whether they **guessed the number correctly**.
* Game keeps running until player chooses to **quit** or **runs out of money**.

---

### **Step 1: Import random**

```python
import random
```

* We need **random numbers** for dice rolls.
* `random.randint(a, b)` → gives a random integer between `a` and `b` (inclusive).
* Dice = 1 to 6 → `random.randint(1,6)`

---

### **Step 2: Setup player money**

```python
player_money = 100  # Starting money
```

* Let’s give player **\$100** to start.
* We’ll **add/subtract** money based on wins/losses.

---

### **Step 3: Main game loop**

```python
while player_money > 0:
    print(f"\nYou have ${player_money}. Let's gamble!")

    # Ask for bet
    bet = int(input("Enter your bet amount: "))

    if bet > player_money:
        print("You don't have that much, dumbass!")
        continue  # Go back to start of loop

    # Ask for guess
    guess = int(input("Guess the dice roll (1-6): "))

    if guess < 1 or guess > 6:
        print("Invalid guess! Only numbers 1-6, idiot!")
        continue
```

* `while player_money > 0:` → game keeps running **while you still have money**.
* Ask **bet** → can’t bet more than you have.
* Ask **guess** → must be 1-6.
* `continue` → skips the rest of the loop if input invalid → **restart loop**.

---

### **Step 4: Roll the dice and check result**

```python
dice = random.randint(1, 6)
print(f"The dice rolled: {dice}")

if guess == dice:
    winnings = bet * 2
    player_money += winnings
    print(f"Fuck yeah! You won ${winnings}!")
else:
    player_money -= bet
    print(f"Lame! You lost ${bet}. Try again!")
```

* `dice` → random roll between 1 and 6.
* If guess correct → **win double the bet**.
* Else → **lose the bet**.
* Updates `player_money` accordingly.

---

### **Step 5: Option to quit**

```python
play_again = input("Do you want to roll again? (yes/no): ").lower()
if play_again != "yes":
    print(f"You leave the table with ${player_money}. Bye, loser!")
    break
```

* Asks if player wants to continue.
* Any answer other than `"yes"` → exit loop → game ends.

---

### **Step 6: Full code (ready to run)**

```python
import random

player_money = 100  # Starting money

while player_money > 0:
    print(f"\nYou have ${player_money}. Let's gamble!")

    bet = int(input("Enter your bet amount: "))

    if bet > player_money:
        print("You don't have that much, dumbass!")
        continue

    guess = int(input("Guess the dice roll (1-6): "))

    if guess < 1 or guess > 6:
        print("Invalid guess! Only numbers 1-6, idiot!")
        continue

    dice = random.randint(1, 6)
    print(f"The dice rolled: {dice}")

    if guess == dice:
        winnings = bet * 2
        player_money += winnings
        print(f"Fuck yeah! You won ${winnings}!")
    else:
        player_money -= bet
        print(f"Lame! You lost ${bet}. Try again!")

    play_again = input("Do you want to roll again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"You leave the table with ${player_money}. Bye, loser!")
        break

if player_money <= 0:
    print("You’re broke, idiot! Game over.")
```

---

### **Step 7: How it executes (step by step)**

1. Player starts with \$100.
2. `while player_money > 0:` → loop starts.
3. Menu-like messages → shows current money.
4. Player enters **bet** → check if valid.
5. Player enters **guess** → check if valid.
6. `dice = random.randint(1,6)` → random roll.
7. Check guess:

   * Correct → win money
   * Wrong → lose money
8. Ask if player wants to continue → `break` if no.
9. Loop repeats **until money = 0** or player quits.
10. Game ends → final money printed.

---

### **Key concepts you’re using**

* `while` loop → repeating game
* `if/else` → checking bet, guess, wins/losses
* `random.randint()` → random dice roll
* Variables → track money, bet, guess, dice, winnings
* `continue` → restart loop if invalid input

---
