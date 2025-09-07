
---

# **Project: Rock-Paper-Scissors Game**

## **What we are building**

* User plays **Rock-Paper-Scissors** against the computer.
* Computer choice = **random**.
* User inputs choice via **console**.
* Compare choices → decide **winner**.
* Keep **score** until user quits.

---

### **Step 1: Import random**

```python
import random
```

* We need **random choice for computer**.
* Computer will pick **rock, paper, or scissors randomly**.

---

### **Step 2: Setup choices and score**

```python
options = ["rock", "paper", "scissors"]  # list of possible moves
user_score = 0
computer_score = 0
```

* `options` → iterable list, like our quiz or dice numbers
* Scores start at 0 → **track wins**

---

### **Step 3: Main game loop**

```python
while True:
    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")
    user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()

    if user_choice == "quit":
        print("You’re leaving the game, pussy. Final score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break

    if user_choice not in options:
        print("Invalid choice, idiot! Try again.")
        continue
```

* `while True:` → loop keeps the game **running until user quits**
* `input()` → user chooses move
* `.lower()` → converts input to lowercase (so `Rock` = `rock`)
* If input = `"quit"` → break loop → exit game
* If invalid → `continue` → restart loop

---

### **Step 4: Computer choice**

```python
computer_choice = random.choice(options)
print(f"Computer chose: {computer_choice}")
```

* `random.choice(options)` → pick **one from list** randomly
* Print computer’s choice

---

### **Step 5: Determine winner**

```python
if user_choice == computer_choice:
    print("Tie! Nobody wins this round.")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("Fuck yeah! You win this round!")
    user_score += 1
else:
    print("You lost this round, loser!")
    computer_score += 1
```

* If **choices match** → tie
* Check all **winning conditions for user** using `or`
* Else → computer wins
* Update **score** accordingly

---

### **Step 6: Full Code (Ready to Run)**

```python
import random

options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:
    print(f"\nScore -> You: {user_score} | Computer: {computer_score}")
    user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()

    if user_choice == "quit":
        print("You’re leaving the game, pussy. Final score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break

    if user_choice not in options:
        print("Invalid choice, idiot! Try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Tie! Nobody wins this round.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Fuck yeah! You win this round!")
        user_score += 1
    else:
        print("You lost this round, loser!")
        computer_score += 1
```

---

### **Step 7: How it executes (step by step)**

1. **Start loop** → scores at 0
2. **User input** → rock, paper, scissors, or quit
3. **Computer randomly picks** → `random.choice(options)`
4. **Compare choices** → determine winner
5. **Update scores** → `user_score` or `computer_score`
6. **Loop continues** → until user types `"quit"`
7. **Print final scores** → game ends

---

### **Step 8: Key concepts you’re using**

* **Lists** → iterable of moves
* **while loop** → repeat game rounds
* **if/elif/else** → decide winner
* **random.choice()** → computer unpredictability
* **Variables** → track scores, choices
* **continue** → restart loop for invalid input

---

