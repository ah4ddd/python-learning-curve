> “A function calls itself and it keeps repeating. **Until what?**”

Here is the answer, clean and final:

---

# THE CORE RULE OF RECURSION (THIS IS NON-NEGOTIABLE)

> **A recursive function MUST have a condition where it stops calling itself.**

That condition is called the **base case**.

If there is **no base case**, the program crashes. Period.

So recursion is **not**:

> “a function that keeps calling itself forever”

It is:

> “a function that calls itself **only while a condition is true**, and stops when it’s false”

---

## Let’s kill the confusion with the simplest possible example

Forget files. Forget trees. Forget pathlib.

### Example 1: Counting down

```python
def countdown(n):
    if n == 0:      # ← STOP CONDITION (base case)
        return
    print(n)
    countdown(n - 1)
```

Call it:

```python
countdown(3)
```

### What ACTUALLY happens step by step

1. `countdown(3)`

   * `n == 0`? No
   * print 3
   * call `countdown(2)`

2. `countdown(2)`

   * `n == 0`? No
   * print 2
   * call `countdown(1)`

3. `countdown(1)`

   * `n == 0`? No
   * print 1
   * call `countdown(0)`

4. `countdown(0)`

   * `n == 0`? **YES**
   * return (STOP)

Then everything unwinds and the program ends.

### Output:

```
3
2
1
```

👉 **It stops when the condition is met.**
That’s it. That’s the entire secret.

---

## Now apply this to FILES (your actual case)

Here is the recursion again, simplified:

```python
def display_tree(directory):
    for item in directory.iterdir():
        print(item.name)
        if item.is_dir():
            display_tree(item)
```

### The STOP CONDITION here is:

```python
if item.is_dir():
```

If the item is **NOT a directory**, the function **does NOT call itself**.

Files are the **base case**.

So the recursion stops automatically when:

* there are no more folders
* only files remain

---

## EXACTLY when does it stop?

Let’s say your structure is:

```
my_project/
├── README.md
├── src/
│   ├── main.py
│   └── utils.py
```

Execution:

1. `display_tree(my_project)`

   * sees `README.md` → not a dir → stop there
   * sees `src/` → is a dir → recurse

2. `display_tree(src)`

   * sees `main.py` → not a dir → stop
   * sees `utils.py` → not a dir → stop

No more directories.

👉 Recursion ends **naturally**.

There is no loop running forever.
There is no counter you forgot.
The filesystem itself guarantees the stop.

---

## THIS is why your brain was stuck

You were missing **one single idea**:

> **Recursion always needs a base case.
> No base case = infinite recursion = crash.**

Every correct recursive function has:

1. **Base case** (when to stop)
2. **Recursive case** (when to repeat with smaller input)

No exceptions.

---

## Why recursion feels alien (but isn’t)

Loops say:

> “Repeat this block N times.”

Recursion says:

> “Solve this problem.
> If there’s a smaller version of the same problem inside it, solve that too.”

Different mindset. Same execution rules.

---

## One sentence that should lock it in permanently

> **Recursion stops when the function reaches a case where it does NOT call itself.**

That’s the answer to your “until what?” question.

