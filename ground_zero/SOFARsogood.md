## 100% Intro to Python done

---

## 🧠 1. Creating Variables

A **variable** stores data — like giving something a name so you can reuse it.

```python
name = "Ahad"        # string
age = 20             # integer
height = 1.8         # float
is_student = True    # boolean
```

➡️ Think of a variable as a *box* with a label and something stored inside.
You can change it anytime:

```python
age = 21
```

---

## ⚙️ 2. Using Variables

You can use variables in expressions, combine them, and print their values.

```python
x = 5
y = 3
z = x + y
print("Sum:", z)     # Output: Sum: 8
```

➡️ When you update a variable, the old value is forgotten — it now holds the new one.

---

## ✅ 3. True and False

Python uses **booleans** to represent truth values:

* `True` means yes
* `False` means no

```python
is_sunny = True
is_raining = False

print(not is_sunny)   # Output: False
```

➡️ `not`, `and`, `or` are **logical operators**:

* `and` → True only if *both* are true
* `or` → True if *at least one* is true
* `not` → flips the value

---

## 🔢 4. Checking Number Equality

We use **comparison operators** to check relationships:

| Operator | Meaning          |
| -------- | ---------------- |
| `==`     | equal to         |
| `!=`     | not equal to     |
| `>`      | greater than     |
| `<`      | less than        |
| `>=`     | greater or equal |
| `<=`     | less or equal    |

```python
a = 10
b = 5
print(a > b)      # True
print(a == b)     # False
print(a != b)     # True
```

➡️ All comparisons return `True` or `False`.

---

## 💬 5. Formatting Strings

F-strings let you mix variables and text cleanly using `{}`:

```python
name = "Ahad"
age = 20
print(f"My name is {name} and I am {age} years old.")
```

➡️ You can also use expressions inside:

```python
print(f"Next year, I’ll be {age + 1}.")
```

➡️ Without `f`, `{}` won’t work — it’ll just print literally `{}`.

---

## 🤖 6. Python Basics Practice (Mini recap)

You practiced combining everything — variables, expressions, strings, booleans.
Example:

```python
likes = 50
print(f"Post has {likes} likes")
```

---

## 💬 7. Bot (Part 1)

Your first small **bot conversation** project — putting all basics together:

```python
print("Hello! What is your name?")
name = "Ahad"
print(f"Nice to meet you, {name}!")
```

---

## 🔢 8. Comparing Numbers

You learned number comparisons like:

```python
score = 90
passing = 75
print(score > passing)  # True
```

---

## 🆚 9. Comparing Strings

Strings can be compared alphabetically:

```python
print("Tokyo" < "Zurich")  # True, because T comes before Z
```

➡️ They’re compared **letter by letter** based on Unicode values.

---

## 🧩 10. Discovering Types

You checked what kind of data a variable holds using `type()`:

```python
x = 10
print(type(x))        # <class 'int'>

y = "hello"
print(type(y))        # <class 'str'>
```

---

## 🔄 11. Type Conversion

You converted one type into another:

```python
age = "17"
converted_age = int(age)
print(converted_age + 1)   # 18
```

Common conversion functions:

* `int()` → to integer
* `float()` → to decimal
* `str()` → to string
* `bool()` → to True/False

Examples:

```python
print(int(True))    # 1
print(int(False))   # 0
print(bool(0))      # False
print(bool("Hi"))   # True
```

---

## ⌨️ 12. Input

You learned to take **user input**:

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

All inputs come as **strings**, so convert if needed:

```python
age = int(input("How old are you? "))
print(f"Next year you’ll be {age + 1}.")
```

---

## 🤖 13. Bot (Part 2 — Interactive Bot)

You built your **interactive bot**:

```python
name = input("What's your name? ")
age = int(input("How old are you? "))
color = input("What's your favorite color? ")

print(f"Hey {name}! You’re {age} years old and love {color}. Cool!")
```

This project combined:
✅ Input
✅ Type conversion
✅ String formatting
✅ Printing
✅ Logic flow

---

## 🧱 FINAL TAKEAWAY

Blunt summary:

> You now know how to make Python **store**, **compare**, **format**, **convert**, and **interact**.
> You’ve mastered the foundation of the language — variables, data types, logic, and input/output.

From here, you can build **calculators, bots, small tools, or logic-based systems** easily.

---
