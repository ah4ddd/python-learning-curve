### **What “Reusing Code” Means**

Imagine you’re writing a program where you greet 5 people:

```python
print("Hello, Ahad!")
print("Hello, Babe!")
print("Hello, Mom!")
print("Hello, Dad!")
print("Hello, Friend!")
```

* Look at that mess? If you want to change “Hello” to “Hi”, you have to rewrite it **5 times**.
* Not smart. Not efficient. Not scalable.

**Solution:** put that code in a **function** and just **call it** whenever you need it.

---

### **Step 1: Define a Function to Reuse**

```python
def greet(name):
    print(f"Hello, {name}!")
```

* `greet` = function name.
* `name` = input (parameter).
* Code inside runs **every time** you call it.

---

### **Step 2: Call the Function Multiple Times**

```python
greet("Ahad")
greet("Babe")
greet("Mom")
greet("Dad")
greet("Friend")
```

**Output:**

```
Hello, Ahad!
Hello, Babe!
Hello, Mom!
Hello, Dad!
Hello, Friend!
```

* Now you wrote the greeting code **once**, but reused it **5 times**.
* Want to change the greeting? Only **change it inside the function**, not everywhere.

---

### **Step 3: Reuse With Calculations**

Functions aren’t just for printing. They can **calculate things** and you can reuse that logic too.

```python
def add(a, b):
    return a + b

print(add(5, 3))
print(add(10, 20))
print(add(7, 9))
```

**Output:**

```
8
30
16
```

* You wrote the **add logic once**, reused it multiple times with different numbers.
* If you want to fix a bug or change the logic, only one place to update.

---

### **Step 4: Mini Project Example – Reusing Code**

Imagine you’re building a **mini sales tracker**:

```python
def record_sale(product, quantity):
    print(f"Recorded sale: {quantity} units of {product}")

# Reusing function for multiple products
record_sale("Soap", 5)
record_sale("Cake", 3)
record_sale("Bread", 7)
```

**Output:**

```
Recorded sale: 5 units of Soap
Recorded sale: 3 units of Cake
Recorded sale: 7 units of Bread
```

* Instead of writing `print(f"Recorded sale: {x} units of y")` for every product, you **reused a single function**.

---

### **Key Takeaways**

1. **Define once, use many times.** That’s the core of functions.
2. **Parameters let you customize behavior** without rewriting code.
3. Makes your code **clean, readable, and maintainable**.
4. **Changing logic?** Change in function → automatically updated everywhere it’s called.

---

### **Memory Picture**

Think of it like a **robot in your code**:

* You program the robot once (function definition).
* You tell it “do this for Ahad, then do it for Babe” (function calls).
* Robot executes the same logic, but with different inputs. ✅

---

Tomorrow, we can move to the next level: **Return Values + Using Function Outputs** so your functions can actually **give data back** and not just print stuff.

---

