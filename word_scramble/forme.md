
---

# **“Word Scramble Game”**

**What it does:**

* Game picks a random word from a list.
* Scrambles the letters.
* Player must **guess the correct word**.
* Tracks attempts, shows hints (word length), and gives feedback.
* Uses everything: loops, lists, strings, input, random, f-strings, conditionals.

---

# **Line-by-Line Explanation**

### **1. `import random`**

* Same as before → lets us **pick random word** and **shuffle letters**.

### **2. Word list**

```python
words = ["python", "hangman", "developer", "function", "variable", "algorithm"]
```

* A **list of words** player might get.
* Shows **lists in action** → ordered collection of strings.

### **3. Pick random word**

```python
word = random.choice(words)
```

* Picks **one word randomly** from the list.
* Fundamental: **using randomness in games**.

### **4. Scramble the word**

```python
scrambled = list(word)  # word -> list of letters
random.shuffle(scrambled)  # shuffle letters
scrambled_word = "".join(scrambled)  # list -> string
```

* `list(word)` → converts `"python"` → `["p","y","t","h","o","n"]`
* `random.shuffle(scrambled)` → **randomly rearranges letters**
* `"".join(scrambled)` → **turns list of letters back into a string**
* ✅ Teaches **string/list conversion, join, shuffle**

### **5. Set attempts**

```python
attempts = len(word) + 3
```

* Uses **len()** to **calculate word length** → add 3 extra tries

### **6. Welcome message**

```python
print(f"Unscramble this word: {scrambled_word}")
print(f"The word has {len(word)} letters. You have {attempts} attempts. Good luck, dumbass!")
```

* `f""` → inserts variables dynamically
* Shows **scrambled word, length, attempts**

### **7. Game loop**

```python
while attempts > 0:
```

* Keep asking player until **out of attempts**

### **8. Take guess**

```python
guess = input("Your guess: ").lower()
```

* `input()` → player types guess
* `.lower()` → makes it **case-insensitive**

### **9. Check correctness**

```python
if guess == word:
    print("Fuck yeah! You got it right!")
    break
```

* If **correct guess**, game ends.

### **10. Wrong guess**

```python
else:
    attempts -= 1
    print(f"Wrong, idiot! Attempts left: {attempts}")
```

* Wrong guess → **reduce attempts**, give feedback

### **11. Optional hint**

```python
if attempts == len(word) + 1:
    print(f"Hint: first letter is '{word[0]}'")
```

* After **2 wrong attempts**, give **first letter hint**

### **12. Game over**

```python
if attempts == 0:
    print(f"Game over, loser! The word was '{word}'")
```

* Player failed → reveal word

---

# **execution**

➜ word_scramble git:(main) python3 ws.py
Welcome to Word Scramble!
Unscramble this word: nufcniot
The word has 8 letters. You have 11 attempts. Good luck, dumbass!
Your guess: function
Fuck yeah! You got it right!

---

# **What You’re Learning Here**

* **Randomness** → pick words, shuffle letters
* **Lists & strings** → convert, join, manipulate
* **Loops & conditionals** → run game logic, handle correct/wrong guesses
* **f-strings** → insert variables dynamically
* **Input handling** → `.lower()`, validation, user feedback
* **State tracking** → attempts, hints, game over

---
