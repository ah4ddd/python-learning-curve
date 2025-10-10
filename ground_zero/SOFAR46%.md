
---

## **Python Basics Cheat Sheet (so far)**

### **1. Variables**

* Store **data** (numbers, strings, booleans).
* Syntax:

```python
name = "Ahad"      # string
age = 20           # number
available = True   # boolean
```

* Can update anytime:

```python
age = age + 1
```

---

### **2. Expressions**

* Any **operation that produces a value**.
* Can include variables, math, or logic:

```python
x = 5
y = 3
total = x + y      # 8 → stored in total
```

---

### **3. Booleans**

* Only **True** or **False**.
* Created by **comparisons or logic**:

```python
x = 5
y = 10
print(x < y)       # True
print(x == y)      # False
```

* Logical operators: `and`, `or`, `not`

---

### **4. Comparison Operators**

| Operator | Meaning               |
| -------- | --------------------- |
| `==`     | equal                 |
| `!=`     | not equal             |
| `<`      | less than             |
| `>`      | greater than          |
| `<=`     | less than or equal    |
| `>=`     | greater than or equal |

---

### **5. F-Strings (Formatted Strings)**

* Use `f""` to **insert variables, expressions, functions, logic** into strings.
* Syntax:

```python
name = "Ahad"
age = 22
print(f"My name is {name} and I will be {age + 1} next year.")
```

* Can include:

  * **Variables:** `{name}`
  * **Expressions:** `{age + 1}`
  * **Function calls:** `{len(name)}`
  * **Inline logic:** `{ "adult" if age >= 18 else "minor" }`
  * **Multiple placeholders:** `{var1} {var2} {var3}`
  * **Decimal formatting:** `{balance:.2f}`
* Can store f-strings in a **variable** or **return from a function** for reuse.

---

### **6. Functions (Mini Intro)**

* Reusable **blocks of code** that can take input (`parameters`) and give output (`return`).

```python
def greet(user_name):
    return f"Hello, {user_name.upper()}!"
print(greet("Ahad"))  # Hello, AHAD!
```

---

### **7. Printing**

* `print()` outputs **any value** to console.
* Can combine text and variables using **f-strings** or `+` for strings:

```python
score = 100
print("Score: " + str(score))      # old way
print(f"Score: {score}")           # f-string way ✅
```

---
