
---

# **1️⃣ Making Decisions (if statements)**

**Concept:**

* `if` statements let the program **decide what to do based on a condition**.
* Condition is usually a comparison (e.g., `==`, `<`, `>`).

**Syntax:**

```python
if condition:
    # code to run if condition is True
```

**Example:**

```python
age = 18
if age >= 18:
    print("You are an adult.")
```

* Output: `You are an adult.`
* ✅ If the condition is false, nothing happens.

---

# **2️⃣ Using Conditions**

**Concept:**

* Conditions are expressions that evaluate to `True` or `False`.
* Can compare numbers, strings, booleans.

**Operators:**

* `==` → equals
* `!=` → not equals
* `>` , `<` , `>=` , `<=` → greater, less, etc.

**Example:**

```python
score = 85
if score >= 90:
    print("Grade A")
else:
    print("Not A")
```

* Output: `Not A`

---

# **3️⃣ Conditional Statements 1 (practice)**

**Practice idea:**

```python
temperature = 30
if temperature > 25:
    print("It's hot outside!")
```

* Simple check → runs code **only if condition is True**.

---

# **4️⃣ Coding Else Statements**

**Concept:**

* `else` runs **when the `if` condition is False**.

**Syntax:**

```python
if condition:
    # do this if True
else:
    # do this if False
```

**Example:**

```python
num = 10
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

* Output: `Even`
* ✅ Always one path executes.

---

# **5️⃣ Incorporating Elif**

**Concept:**

* `elif` = “else if” → allows **multiple conditions**.
* Lets you check **more than one case**.

**Syntax:**

```python
if condition1:
    # do this
elif condition2:
    # do that
else:
    # fallback
```

**Example:**

```python
marks = 75
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")
```

* Output: `B`

**Key point:**

* Checks **top-down** → first True executes, others skipped.

---

# **6️⃣ Using Complex Decisions**

**Concept:**

* Combine conditions using `and`, `or`, `not`.

**Examples:**

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed to enter club")
```

* Output: `Allowed to enter club`

```python
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend!")
```

* Output: `Weekend!`

```python
logged_in = False
if not logged_in:
    print("Please log in")
```

* Output: `Please log in`

---

# **7️⃣ Conditional Statements 2 (practice)**

**Example combining all:**

```python
temp = 35
rain = False

if temp > 30 and not rain:
    print("Go to the beach")
elif temp > 20 and rain:
    print("Take umbrella for walk")
else:
    print("Stay home")
```

* ✅ Combines `if`, `elif`, `else`, `and`, `not`.

---

# **8️⃣ Rock-Paper-Scissors (part 1)**

**Concept:**

* Apply all previous decisions to **game logic**.
* Player vs computer → compare choices → decide winner.

**Basic example:**

```python
import random

player = input("rock, paper, or scissors? ").lower()
computer = random.choice(["rock", "paper", "scissors"])

if player == computer:
    print("Tie")
elif player == "rock" and computer == "scissors":
    print("Player wins")
elif player == "paper" and computer == "rock":
    print("Player wins")
elif player == "scissors" and computer == "paper":
    print("Player wins")
else:
    print("Computer wins")
```

* ✅ This is **decision-making in action**.

---

# **9️⃣ Self-assigning and Operators**

**Concept:**

* `+=`, `-=`, `*=`, `/=` → update variables easily.

**Example:**

```python
score = 0
score += 1  # same as score = score + 1
score *= 2  # multiply by 2
print(score)
```

* Output: `2`

* Used for **tracking score in games**.

---

# **🔟 While Loops**

**Concept:**

* Repeats code **while a condition is True**.

**Syntax:**

```python
while condition:
    # code block
```

**Example:**

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

* Output: `0 1 2 3 4`

---

# **11️⃣ Stopping While Loops**

**Methods:**

* Change the condition → eventually becomes False.
* Use `break` to exit immediately.

**Example:**

```python
while True:
    answer = input("Type 'exit' to quit: ")
    if answer == "exit":
        break
```

* ✅ Infinite loop with `break` for quit functionality.

---

# **12-17️⃣ For Loops and Advanced Loop Control**

**For loop concept:**

* Repeats code **a fixed number of times** over a sequence (like list, range).

**Syntax:**

```python
for i in range(5):
    print(i)
```

* Output: `0 1 2 3 4`

**Advanced loop control:**

* `continue` → skip current iteration
* `break` → exit loop early

**Example:**

```python
for i in range(1, 6):
    if i == 3:
        continue  # skip printing 3
    print(i)
```

* Output: `1 2 4 5`

---

# **18️⃣ Rock-Paper-Scissors (advanced)**

* **Combine everything**: while loops + for loops + scoring + quit.
* This is the **project we just upgraded**.
* Uses:

  * `while True` for rounds
  * `if/elif/else` for game decisions
  * `+=` operators for score
  * `break` for quitting
  * Input validation

**Example:** (from your upgraded code)

```python
# code we fixed earlier with score, rounds, and quit
```

* ✅ Everything learned so far is **applied in a single game**.

---

# ✅ Summary

* **Decisions:** `if`, `elif`, `else`
* **Operators:** `==`, `!=`, `>`, `<`, `>=`, `<=`, `and`, `or`, `not`
* **Loops:** `while` (dynamic), `for` (fixed)
* **Loop control:** `break`, `continue`
* **Self-assigning:** `+=`, `-=`, etc.
* **Projects:** Rock-Paper-Scissors (basic → advanced), applying all above.

**Takeaway:**

* You’ve learned **flow control**, **decision-making**, and **looping**, and already applied it to **real interactive games**.
* All the pieces now fit together for **any small Python game or interactive app**.

---
