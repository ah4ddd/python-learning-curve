## ✨ Python Ternary (Conditional) Expression

A **ternary expression** in Python is a compact way to choose between two values based on a condition. It evaluates a condition and **produces one of two values**. Think of it as a mini *if/else* that fits on one line.

### 🔧 Syntax

```python
value_if_true if condition else value_if_false
```

Read this in plain English as:

> “Give me `value_if_true` if the condition is true, otherwise give me `value_if_false`.”

Notice that the **value for the True case comes first**, which might feel reversed if you’re thinking in traditional `if/else` order.

---

### 💡 Example

```python
age = 20
status = "adult" if age >= 18 else "minor"
```

Explanation:

* If `age >= 18` is True, the expression becomes `"adult"`
* Otherwise, it becomes `"minor"`
* The final value gets assigned to `status`

---

### 🔍 Important idea

A ternary expression **does not execute statements** like a normal `if`.
It only **evaluates into a value**.

Compare:

#### Normal if-statement

```python
if condition:
    x = "yes"
else:
    x = "no"
```

#### Ternary expression

```python
x = "yes" if condition else "no"
```

Both set `x`, but the ternary does it in one expression.

---

### 🌈 Where it’s useful

Use a ternary when:

* You need to choose **a value**, not run multiple lines of logic
* The decision is simple
* The code becomes more readable in one line

Examples:

```python
color = "green" if score > 50 else "red"
```

```python
result = "WIN" if pick in lucky_list else "LOSE"
```

---

### ⚠️ When to avoid it

Avoid ternaries if:

* The condition is long and complicated
* The values are long or complex
* Readability becomes worse instead of better

In those cases, a normal `if/else` is clearer.

---

### TL;DR

* It’s called a **ternary** because it has 3 parts
* It chooses between two values
* It does **not** run blocks of code
* It’s basically a one-line value selector
* Use it when it improves clarity, not just to shorten code
