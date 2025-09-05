
---

## **Step 1: What the To-Do List Will Do**

1. Allow you to **add tasks**.
2. Allow you to **remove tasks** by number.
3. Show you the **list of all tasks**.
4. Keep running until you choose to **quit**.

Basically, it’s a **mini productivity boss tool** in your terminal. 📝

---

## **Step 2: The Full Code**

```python
# 1. Welcome the user
print("Welcome to your savage To-Do List, let's get shit done!")

# 2. Create an empty list to store tasks
tasks = []

# 3. Start infinite loop so user can keep managing tasks
while True:
    # 4. Show options to the user
    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. List tasks")
    print("4. Quit")

    # 5. Get user choice
    choice = input("Choose an option (1-4): ")

    # 6. Add a task
    if choice == '1':
        task = input("Enter the task you lazy bastard: ")
        tasks.append(task)
        print(f"Task added: {task}")

    # 7. Remove a task
    elif choice == '2':
        if not tasks:
            print("No tasks to remove, you slacker!")
            continue
        # Show tasks with numbers
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid number, idiot!")

    # 8. List all tasks
    elif choice == '3':
        if not tasks:
            print("No tasks, you’re chilling too much!")
        else:
            print("Your savage tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    # 9. Quit
    elif choice == '4':
        print("Exiting To-Do List. Go conquer the world, champ!")
        break

    # 10. Invalid input
    else:
        print("Invalid choice, try again you fool!")
```

---

## **Step 3: Line-by-Line Brutal Explanation**

### **Line 1: Welcome**

```python
print("Welcome to your savage To-Do List, let's get shit done!")
```

* Just says hello. Sets the **vibe**. 🔥

---

### **Line 2: Create task storage**

```python
tasks = []
```

* `tasks` is an **empty list** where all your tasks will live.
* Lists are **like arrays** in Python—you can add, remove, and loop through them.

---

### **Line 3: Infinite loop**

```python
while True:
```

* Keep the program running forever until user quits.
* Allows continuous adding/removing/listing tasks.

---

### **Line 4: Show menu**

```python
print("\nOptions:")
print("1. Add task")
print("2. Remove task")
print("3. List tasks")
print("4. Quit")
```

* Shows the user what they can do every loop.
* `\n` adds a blank line for readability.

---

### **Line 5: Get user choice**

```python
choice = input("Choose an option (1-4): ")
```

* Waits for the player to type something.
* Stores it in `choice`.

---

### **Line 6: Add task**

```python
if choice == '1':
    task = input("Enter the task you lazy bastard: ")
    tasks.append(task)
    print(f"Task added: {task}")
```

* `input()` = ask what the task is.
* `tasks.append(task)` = adds the task to the **end of the list**.
* Print confirmation.

---

### **Line 7: Remove task**

```python
elif choice == '2':
    if not tasks:
        print("No tasks to remove, you slacker!")
        continue
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")
    task_num = int(input("Enter task number to remove: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid number, idiot!")
```

* First, check if there are tasks.
* `enumerate(tasks, 1)` = numbers tasks starting at 1.
* `tasks.pop(index)` = removes task at that **index**.
* Index in Python **starts at 0**, so we do `task_num - 1`.

---

### **Line 8: List tasks**

```python
elif choice == '3':
    if not tasks:
        print("No tasks, you’re chilling too much!")
    else:
        print("Your savage tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
```

* Show all tasks with numbers.
* Easy to see what you’ve got to do.

---

### **Line 9: Quit**

```python
elif choice == '4':
    print("Exiting To-Do List. Go conquer the world, champ!")
    break
```

* Breaks the infinite loop → exits program.

---

### **Line 10: Invalid input**

```python
else:
    print("Invalid choice, try again you fool!")
```

* Anything other than 1-4 → insult them and loop again.

---

## ✅ **Step 4: How to Run It**

1. Save as `todo.py`.
2. Open terminal → navigate to folder.
3. Run:

```bash
python3 todo.py
```

* Add tasks → remove tasks → list tasks → quit.

---

