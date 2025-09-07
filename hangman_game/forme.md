
---

# **Full Code We’re Explaining (Option-Based Hangman)**

```python
import random

full_list = ["python", "hangman", "computer", "programming", "developer", "algorithm", "function", "variable"]

options = random.sample(full_list, 5)
word = random.choice(options)

guessed_letters = []
wrong_letters = []
attempts = 6

print("Welcome to Hangman, loser!")
print("Here are your possible words:")
print(", ".join(options))
print(f"The word has {len(word)} letters. Good luck, dumbass!")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print(f"\nWord: {display_word}")
    print(f"Wrong guesses: {', '.join(wrong_letters)}")

    if "_" not in display_word:
        print("Fuck yeah! You guessed the word and won!")
        break

    guess = input("Guess a single letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("One letter only, dumbass!")
        continue

    if guess in guessed_letters or guess in wrong_letters:
        print("You already tried that, idiot!")
        continue

    if guess in word:
        print(f"Nice! The letter '{guess}' is in the word.")
        guessed_letters.append(guess)
    else:
        print(f"Wrong! '{guess}' is not in the word.")
        wrong_letters.append(guess)
        attempts -= 1
        print(f"You have {attempts} attempts left, loser!")

if attempts == 0:
    print(f"Game over, idiot! The word was '{word}'.")
```

---

# **Line-By-Line Explanation**

### **1. `import random`**

* Brings Python’s **random module** into the program.
* Lets us **pick random items** from a list (words for Hangman).
* Without this, the computer would **always give the same word**, which is boring.

---

### **2. `full_list = ["python", ...]`**

* Creates a **list of strings**. Each string is a **word player might guess**.
* Lists are **ordered collections** → we can access items, pick random items, loop through them.
* Example: `full_list[0]` → `"python"`.

---

### **3. `options = random.sample(full_list, 5)`**

* `random.sample(list, n)` → picks **5 unique items randomly** from `full_list`.
* `options` → the **five words player will see as hints**.
* This prevents the game from being a **pure blind guess**.

---

### **4. `word = random.choice(options)`**

* `random.choice(list)` → picks **one item randomly** from `options`.
* This is the **actual word to guess**.
* The rest of the code works with `word`.

---

### **5. `guessed_letters = []`**

* Empty **list to store letters the player guessed correctly**.
* Example: if word is `"python"` and player guesses `"h"`, list becomes `["h"]`.

---

### **6. `wrong_letters = []`**

* Empty **list to store letters the player guessed incorrectly**.
* Helps **show player what they already guessed and failed**.

---

### **7. `attempts = 6`**

* **Max number of wrong guesses** allowed before the game ends.
* Classic Hangman rule: **6 wrong attempts = game over**.

---

### **8. Welcome messages**

```python
print("Welcome to Hangman, loser!")
print("Here are your possible words:")
print(", ".join(options))
print(f"The word has {len(word)} letters. Good luck, dumbass!")
```

* `print()` → displays messages to player.
* `", ".join(options)` → turns **list into readable string**, separated by commas.
* `len(word)` → tells **number of letters in the word** → hint.
* Crude messages make it **fun, engaging, and memorable**.

---

### **9. `while attempts > 0:`**

* **Main game loop**.
* “Keep playing while player still has attempts left.”
* Anything **indented under this** repeats **every round**.

---

### **10. Build the display word**

```python
display_word = ""
for letter in word:
    if letter in guessed_letters:
        display_word += letter
    else:
        display_word += "_"
```

* `display_word` → string showing **progress of guessed letters**.
* `for letter in word:` → loops through **every letter** in the word.
* If letter guessed → show it.
* Else → show `_`.
* Example: `"hangman"` with guesses `["h","a","n"]` → display `"han__an"`.

---

### **11. Print word and wrong guesses**

```python
print(f"\nWord: {display_word}")
print(f"Wrong guesses: {', '.join(wrong_letters)}")
```

* `\n` → adds a new line for readability.
* Shows **current progress** + **wrong letters guessed**.
* Helps player **guess strategically**.

---

### **12. Win check**

```python
if "_" not in display_word:
    print("Fuck yeah! You guessed the word and won!")
    break
```

* If there are **no underscores left**, player guessed all letters → **win**.
* `break` → exits the **while loop**.

---

### **13. Ask for a guess**

```python
guess = input("Guess a single letter: ").lower()
```

* `input()` → pauses program for player to **type something**.
* `.lower()` → converts to lowercase → `"H"` = `"h"`.

---

### **14. Input validation**

```python
if len(guess) != 1 or not guess.isalpha():
    print("One letter only, dumbass!")
    continue
```

* Rejects **multi-letter guesses or numbers**.
* `isalpha()` → checks if it’s a letter.
* `continue` → skips rest of loop, asks again.

---

### **15. Check for repeated guesses**

```python
if guess in guessed_letters or guess in wrong_letters:
    print("You already tried that, idiot!")
    continue
```

* Prevents **wasting attempts on same letter**.

---

### **16. Check if guess is correct**

```python
if guess in word:
    print(f"Nice! The letter '{guess}' is in the word.")
    guessed_letters.append(guess)
else:
    print(f"Wrong! '{guess}' is not in the word.")
    wrong_letters.append(guess)
    attempts -= 1
    print(f"You have {attempts} attempts left, loser!")
```

* If letter in word → **add to guessed\_letters** → reveal it next round.
* Else → **add to wrong\_letters**, reduce `attempts` by 1 → player is punished.

---

### **17. Game over**

```python
if attempts == 0:
    print(f"Game over, idiot! The word was '{word}'.")
```

* If player **ran out of attempts**, reveal the word.

---

# **Python Concepts You Learned Here**

1. **Lists** → word list, guessed letters, wrong letters
2. **Strings** → letters, word display, formatting (`f""`)
3. **Loops** → `while` (game loop), `for` (iterate word letters)
4. **Conditionals** → check letter correctness, win/lose conditions
5. **Random module** → random word, options
6. **Input/Output** → `input()` and `print()`
7. **String methods** → `.lower()`, `join()`
8. **Variables** → track state: attempts, letters guessed
9. **Game logic design** → sequence, feedback, player state

---

## **1. `len()`**

* `len()` is a **built-in Python function**.
* It **counts the length of something**.
* Examples:

```python
word = "python"
len(word)   # 6, because "p","y","t","h","o","n" → 6 letters

options = ["python", "hangman", "computer"]
len(options)  # 3, because there are 3 items in the list

guess = "a"
len(guess)  # 1, because only 1 character
```

✅ **Takeaway:** `len()` tells Python **how many items or letters** are in a string, list, tuple, etc.

---

## **2. `print(f"...{len(word)}...")` and `{}`**

* The `{}` inside `f"..."` is **f-string formatting**.
* `f""` means **"format string"** → Python replaces `{}` with the value of whatever is inside.

Example:

```python
word = "hangman"
print(f"The word has {len(word)} letters")
```

* Python sees `{len(word)}` → calculates `len(word)` → 7 → replaces `{}`
* Output: `"The word has 7 letters"`

✅ **Takeaway:** `{}` lets you **insert variables, calculations, anything dynamic** into a string.

---

## **3. `print(", ".join(options))`**

* `join()` is a **string method**.
* It **joins a list of strings** into one string **with a separator**.

Example:

```python
options = ["python", "hangman", "computer"]
", ".join(options)  # "python, hangman, computer"
```

* The string before `.join()` → `", "` → is **inserted between items**.
* Without it → `''.join(options)` → `"pythonhangmancomputer"` → no commas.

✅ **Takeaway:** Use `join()` to **make lists readable** for printing.

---

## **4. The `display_word` loop**

```python
display_word = ""
for letter in word:
    if letter in guessed_letters:
        display_word += letter
    else:
        display_word += "_"
```

* `display_word = ""` → start with an **empty string**
* `for letter in word:` → **loop through each letter** in the word

Example: `word = "python"`

* First iteration: `letter = "p"`

* Second iteration: `letter = "y"`

* …and so on

* `if letter in guessed_letters:` → check if **player guessed this letter**

* `display_word += letter` → **add the letter to display string**

* `else: display_word += "_"` → if **not guessed**, add `_`

* At the end of the loop → `display_word` becomes something like: `"p__h__"` depending on guesses

✅ **Takeaway:** This **creates the word display dynamically**, showing guessed letters and hiding unknown ones.

---

## **5. Why `_` shows a lot**

* Each iteration of `for letter in word` adds **one character** to `display_word`
* `_` is added for each **letter not guessed**
* So for `"hangman"` (7 letters) → `_ _ _ _ _ _ _`
* Python **doesn’t add spaces automatically**, you just see `"_______"` → but you can print with spaces:

```python
print(" ".join(display_word))  # h _ n _ _ _ _
```

---

## **6. Double quotes `""`**

* `""` → **empty string**, nothing inside
* Used to **initialize a string** or **create an empty string to add to**

Example:

```python
display_word = ""  # empty, we will build it
display_word += "h" # now display_word = "h"
```

✅ **Takeaway:** `""` is just **a blank string to start building something**.

---

## **7. `guess.isalpha()`**

* `.isalpha()` → **checks if string contains only letters**
* Returns `True` or `False`

Example:

```python
"a".isalpha()      # True
"abc".isalpha()    # True
"1".isalpha()      # False
"!".isalpha()      # False
```

* We use it to **prevent numbers, symbols, or multiple letters** from being accepted as a guess.

---

## **8. `in` and `or`**

### **`in`**

* Checks **membership**

* `"a" in "apple"` → True

* `"b" in "apple"` → False

* `"python" in ["python", "hangman"]` → True

* Used in our code to check if:

  * Letter is in word → correct guess
  * Letter is already guessed → prevent repeat

### **`or`**

* Logical operator → **either condition True → whole True**

Example:

```python
if len(guess) != 1 or not guess.isalpha():
    print("One letter only!")
```

* `len(guess) != 1` → guess is not 1 letter
* `not guess.isalpha()` → guess is not a letter
* `or` → **if either of these is True → condition triggers**

✅ **Takeaway:** `in` → checks membership; `or` → checks multiple conditions.

---

# **Putting it all together**

1. **Pick word options** → player sees choices
2. **Pick secret word** → player guesses letters
3. **Loop through each round** → display `_` for unknown letters, show guessed letters
4. **Input validation** → only letters, one at a time
5. **Track guessed and wrong letters** → give feedback
6. **Reduce attempts for wrong guesses** → classic Hangman
7. **Win/Lose check** → tell player outcome

---

