
---

# 🧠 **THE ULTIMATE FOR LOOP CHEAT SHEET**

---

## 💡 What a `for` loop actually does

👉 It **repeats** code for **each item** in a sequence (like a list, range, or string).
You can read it like this:

> “For each thing in this bunch of things, do this action.”

Example:

```python
for i in range(5):
    print(i)
```

👀 means → “For each number from 0 to 4, print it.”

Output:

```
0
1
2
3
4
```

---

## 🧩 1. Looping with `range()`

Range creates a *sequence of numbers*.

### 🧮 Basic

```python
for i in range(1, 6):
    print(i)
```

➡️ Counts from 1 to 5 (never includes the stop number).

---

### 🏃‍♂️ With step (skip numbers)

```python
for i in range(0, 11, 2):
    print(i)
```

➡️ Output: 0, 2, 4, 6, 8, 10

---

### 🌀 Counting backwards

```python
for i in range(10, 0, -1):
    print(i)
```

➡️ Counts from 10 down to 1

---

## 🍎 2. Looping over a list

You can loop directly through items in a list.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I love {fruit}")
```

Output:

```
I love apple
I love banana
I love cherry
```

---

## 🧠 3. Looping through a string

```python
for char in "Ahad":
    print(char)
```

➡️ Loops through each letter.

---

## 🔢 4. `enumerate()` → index + value

```python
names = ["Ahad", "Lily", "Rohan"]

for index, name in enumerate(names):
    print(index, name)
```

Output:

```
0 Ahad
1 Lily
2 Rohan
```

---

## 🔗 5. `zip()` → Loop multiple lists together

```python
names = ["Ahad", "Lily"]
ages = [23, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

Output:

```
Ahad is 23
Lily is 22
```

---

## 🧮 6. Loop + condition (`if` inside `for`)

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
```

Output:

```
2 is even
4 is even
6 is even
8 is even
10 is even
```

(`%` = modulus → gives *remainder*, so `% 2 == 0` means “divides evenly” → even number)

---

## 🧱 7. `break` and `continue`

### 🔻 `break` → stops loop instantly

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

Output:

```
1
2
```

---

### ⚡ `continue` → skip current loop round

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```
1
2
4
5
```

---

## 🧩 8. Nested `for` loops

Loop inside another loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
```

Output:

```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
```

---

## 🎯 9. `for` + `else`

This is rare but useful:
The `else` runs **only if the loop finishes normally (no break)**.

```python
for i in range(3):
    print(i)
else:
    print("Loop finished successfully!")
```

Output:

```
0
1
2
Loop finished successfully!
```

If there was a `break` in the loop, the `else` wouldn’t run.

---

## ⚙️ 10. List comprehension (the shortcut loop)

This is an *advanced* but super common Python trick.

Instead of writing:

```python
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)
```

You can write:

```python
squares = [i ** 2 for i in range(1, 6)]
print(squares)
```

➡️ Output: `[1, 4, 9, 16, 25]`

---

## 💀 BONUS: Looping through dictionaries

```python
person = {"name": "Ahad", "age": 23, "city": "Mumbai"}

for key, value in person.items():
    print(f"{key}: {value}")
```

Output:

```
name: Ahad
age: 23
city: Mumbai
```

---

## 🧠 Summary Table

| Type                      | Description                 | Example                |
| ------------------------- | --------------------------- | ---------------------- |
| `for i in range()`        | Loop through numbers        | Counting, iteration    |
| `for item in list`        | Loop through elements       | Lists, strings         |
| `for i, v in enumerate()` | With index and value        | Position tracking      |
| `for a, b in zip()`       | Multiple lists together     | Combine sequences      |
| `nested for`              | Loops inside loops          | Grids, multiplication  |
| `for + if`                | Filtering                   | Even/odd checks        |
| `break/continue`          | Stop or skip iteration      | Control flow           |
| `for + else`              | Run code if loop ends clean | Search success/failure |
| `list comprehension`      | One-line for loop           | Fast data creation     |

---

