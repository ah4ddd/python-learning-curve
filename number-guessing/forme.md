## **Step 1: Bring in the random brain**

```python
import random
```

* `import` = “I need this tool for my code.”
* `random` = Python’s built-in module to generate random numbers.
* Without this, the computer can’t secretly pick a number.

Think of it like giving your computer a dice. 🎲

---

## **Step 2: Say hello to the player**

```python
print("Welcome to the number guessing game, loser!")
print("I have picked a number between 1 and 100. Try to guess it!")
```

* `print()` just **shows words on the screen**.
* First line = insult the player (because we’re savage).
* Second line = tells them what to do.
* Basically, we’re **setting the stage** for the game.

---

## **Step 3: Pick a secret number**

```python
number_to_guess = random.randint(1, 100)
```

* `random.randint(1, 100)` = picks a number from 1 to 100 randomly.
* We store that number in the variable `number_to_guess`.
* Think of it like the computer **hiding a treasure** and you have to find it. 🏴‍☠️

---

## **Step 4: Prepare the game loop**

```python
guess = None
attempts = 0
```

* `guess = None` → “I don’t know the player’s guess yet.”
* `attempts = 0` → counter for how many times the player guesses.
* Every time the player guesses, we’ll **add 1** to attempts.

---

## **Step 5: The guessing loop**

```python
while guess != number_to_guess:
```

* `while` = “Keep doing the following as long as this is true.”
* `guess != number_to_guess` → “Keep looping until the guess equals the secret number.”
* Basically: **keep asking until player wins.**

---

## **Step 6: Get the player’s guess**

```python
guess = int(input("Enter your pathetic guess: "))
```

* `input()` = pauses the game, asks the player to type something.
* `int()` = converts the typed text (string) into a number.
* We store that number in `guess`.

Example: player types `38` → `guess` becomes **38**.

---

## **Step 7: Count the attempt**

```python
attempts += 1
```

* `+= 1` = “add 1 to attempts.”
* So every time the player guesses, the game **remembers how many tries** they made.

---

## **Step 8: Check the guess**

```python
if guess < number_to_guess:
    print("Too low! Try harder!")
elif guess > number_to_guess:
    print("Too high! Come on!")
else:
    print(f"Bullseye! You got it in {attempts} tries. Not too shabby.")
```

* `if guess < number_to_guess:` → the guess is too small.
* `elif guess > number_to_guess:` → the guess is too big.
* `else:` → the guess is perfect (player wins).
* `f"...{attempts}..."` → shows how many guesses the player made.

So when you guessed **38** and that was the number, the game said:

> Bullseye! You got it in 12 tries. Not too shabby.

---

### ✅ **Summary of the flow**

1. Say hello → print welcome messages.
2. Pick a secret number → computer thinks of a number.
3. Start guessing loop → keep asking player.
4. Player guesses → convert input to number.
5. Count the guess → attempts += 1.
6. Check → too low, too high, or correct.
7. If correct → congratulate and show attempts → game ends.

---

