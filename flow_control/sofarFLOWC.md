
---

## **1. Making Decisions (If Statements)**

**Concept:**
`if` statements are used to **run a block of code only if a condition is true**.

* Condition = Boolean (True/False).
* Indentation is used to define the code block under `if`.

**Example:**

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

**Explanation:** Only prints if `age >= 18` is True.

---

## **2. Using Conditions**

**Concept:**
You can use operators to make conditions more complex:

* `>` greater than
* `<` less than
* `>=` greater or equal
* `<=` less or equal
* `==` equal
* `!=` not equal

**Example:**

```python
score = 85

if score >= 90:
    print("Excellent!")
elif score >= 75:
    print("Good!")
else:
    print("Needs improvement.")
```

**Explanation:**

* Python checks `if` first.
* If `if` is False, it goes to `elif`.
* If all are False, it goes to `else`.

---

## **3. Conditional Statements 1 (Nested if)**

**Concept:**
You can **nest `if` statements** inside another `if` to check multiple layers of conditions.

**Example:**

```python
age = 20
likes_python = True

if age >= 18:
    if likes_python:
        print("Adult who loves Python!")
    else:
        print("Adult, but not into Python.")
else:
    print("Underage!")
```

**Explanation:**

* Nested `if` only runs if outer `if` is True.
* Helps to check multiple conditions in a hierarchy.

---

## **4. Coding Else Statements**

**Concept:**
`else` acts as a **backup plan** if `if` is False. No condition needed.

**Example:**

```python
available = False

if available:
    print("Item is in stock!")
else:
    print("Out of stock!")
```

**Explanation:**

* `else` automatically triggers when the `if` condition is False.

---

## **5. Incorporating Elif**

**Concept:**

* `elif` = "else if"
* Allows **multiple conditional checks** between `if` and `else`
* Can have many `elif`s, only **one `else`** at the end.

**Example:**

```python
temperature = 25

if temperature > 30:
    print("Hot day!")
elif temperature > 20:
    print("Nice day!")
elif temperature > 10:
    print("Cool day!")
else:
    print("Cold day!")
```

---

## **6. Using Complex Decisions**

**Concept:**

* Combine multiple conditions with `and`, `or`, `not`.
* `and` → True if **both** conditions are True
* `or` → True if **any** condition is True
* `not` → flips the Boolean

**Example:**

```python
age = 22
has_ticket = True

if age >= 18 and has_ticket:
    print("Access granted!")
else:
    print("Access denied!")
```

---

## **7. Conditional Statements 2 (Nested Complex Decisions)**

**Concept:**

* Complex decisions **with nested if/elif/else** allow multiple layers of checks.
* Helps implement real-world scenarios like VIP access.

**Example:**

```python
age = 25
dress_code = "formal"
member = True

if age >= 18:
    if dress_code == "formal":
        if member:
            print("VIP access granted! 🎉")
        else:
            print("Access denied: members only.")
    else:
        print("Access denied: wrong dress code.")
else:
    print("Too young to enter.")
```

**Explanation:**

* Nested structure ensures all conditions are checked in order.
* Only when all nested conditions are True, you get final access.

---

## **8. Rock, Paper, Scissors (Mini Game)**

**Concept:**

* Use `input()` for player choice
* Use `random.choice()` for computer choice
* Determine winner using **nested if/elif/else**

**Example:**

```python
import random

player_choice = input("Choose rock, paper, or scissors: ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock":
    if computer_choice == "scissors":
        print("Rock beats scissors! You win!")
    else:
        print("Paper beats rock! Computer wins!")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("Paper beats rock! You win!")
    else:
        print("Scissors beats paper! Computer wins!")
elif player_choice == "scissors":
    if computer_choice == "paper":
        print("Scissors beats paper! You win!")
    else:
        print("Rock beats scissors! Computer wins!")
```

**Explanation:**

* Nested `if` inside each `elif` checks computer's choice.
* Ensures the game logic covers all combinations.

---

## **9. Self-assigning and Operators**

**Concept:**

* Variables can be **updated with themselves** using `=`
* Numbers: increment, decrement, track dynamic values
* Strings: append more content

**Examples:**

```python
# Numbers
wallet = 5
wallet = wallet + 2  # wallet is now 7
wallet += 3           # wallet is now 10
wallet -= 1           # wallet is now 9

# Strings
name = "Ahad"
name = name + " Lily"  # name becomes "Ahad Lily"
name += " and John"    # name becomes "Ahad Lily and John"
```

**Use Case:**

* Track scores, balances, logs, or append strings dynamically.

---

### ✅ **Summary of Day 3**

* `if` → runs block if True
* `else` → runs block if False
* `elif` → multiple conditions between `if` and `else`
* Nested decisions → check multiple layers of conditions
* `and`, `or`, `not` → combine conditions logically
* Mini game → Rock-Paper-Scissors demonstrates nested decisions and inputs
* Self-assigning → update variables efficiently, for both numbers and strings

---
