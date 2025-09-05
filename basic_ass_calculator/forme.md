## **Step 1: What the calculator will do**

* Ask the user what operation they want: `+`, `-`, `*`, `/`.
* Ask for **two numbers**.
* Perform the operation.
* Show the result.
* Loop forever so you can do as many calculations as you want.

---

## **Step 2: The full code**

```python
# 1. Welcome the user
print("Welcome to the savage calculator, baby!")
print("You can do +, -, *, /")

# 2. Start an infinite loop so we can calculate forever
while True:
    # 3. Get the operation from the user
    operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")

    # 4. Check if the player wants to quit
    if operation.lower() == 'q':
        print("Exiting. Your calculator dreams are over. Bye!")
        break  # stops the loop

    # 5. Get the numbers from the player
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # 6. Perform the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("You can’t divide by zero, genius!")
            continue  # skip rest and go to next loop
        result = num1 / num2
    else:
        print("Invalid operation, moron! Try again.")
        continue  # skip rest and go to next loop

    # 7. Show the result
    print(f"The result is: {result}")
```

---

## **Step 3: Line-by-line simple explanation**

### **Lines 1-2: Say hello**

```python
print("Welcome to the savage calculator, baby!")
print("You can do +, -, *, /")
```

* `print()` just shows text.
* Explains to the player what they can do.

---

### **Line 3: Infinite loop**

```python
while True:
```

* `while True` = “keep doing this forever.”
* The calculator never stops unless player quits.

---

### **Line 4: Get operation**

```python
operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")
```

* `input()` = wait for the user to type.
* `operation` = stores what the user typed.
* We also allow `'q'` to quit the program.

---

### **Line 5: Check quit**

```python
if operation.lower() == 'q':
    print("Exiting. Your calculator dreams are over. Bye!")
    break
```

* `.lower()` = makes sure `'Q'` or `'q'` works.
* `break` stops the infinite loop → calculator exits.

---

### **Line 6: Get numbers**

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
```

* `input()` = wait for number.
* `float()` = convert it to decimal numbers (so we can do 3.5 + 2.1).
* `num1` and `num2` = store the numbers for calculation.

---

### **Line 7: Calculate**

```python
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("You can’t divide by zero, genius!")
        continue
    result = num1 / num2
else:
    print("Invalid operation, moron! Try again.")
    continue
```

* Check what operation the user chose.
* Perform the correct math.
* Special case for **division by zero** → Python freaks if you try `5/0`, so we warn them.
* `continue` = skip the rest of the loop and ask again.

---

### **Line 8: Show result**

```python
print(f"The result is: {result}")
```

* Shows the result of the calculation.
* `f""` lets us put variables inside the string easily.

---

## **Step 4: How to run it**

1. Save as `calculator.py`.
2. Open terminal → navigate to folder.
3. Run:

```bash
python3 calculator.py
```

4. Do your calculations, try `+`, `-`, `*`, `/`.
5. Quit with `'q'`.

---

### ✅ **Step 5: How to make it savage/pro-level next**

* Add **loops for multiple numbers**, not just two.
* Add **power `**` and modulus `%`**.
* Add **memory feature** → store previous result.
* Add **random insults** every time you make a wrong input.

---

