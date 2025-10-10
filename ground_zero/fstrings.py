# F-String Project 🚀

# Variables
name = "Ahad"
age = 20
messages = 7
tasks_completed = 5
tasks_total = 8
pi = 3.14159
balance = 1234.567

# Function
def greet(user_name):
    return f"Hello, {user_name.upper()}!"

# Expressions & math
tasks_remaining = tasks_total - tasks_completed
messages_plus_tasks = messages + tasks_remaining

# Inline logic
performance = "excellent" if tasks_completed / tasks_total > 0.75 else "average"

# Dashboard display using f-strings
print(f"{greet(name)}")  # Function inside f-string

print(f"Age next year: {age + 1}")  # Expression inside f-string

print(f"You have {messages} unread messages and {tasks_remaining} tasks remaining.")
print(f"Total items to check today: {messages_plus_tasks}")  # Expression with variables

print(f"Your current balance: ${balance:.2f}")  # Formatting float to 2 decimals
print(f"Rounded Pi value: {pi:.3f}")           # Formatting float to 3 decimals

print(f"Task performance: {performance}")  # Inline logic

# Nested expressions
print(f"If you double your remaining tasks: {tasks_remaining * 2}")

# Multiple placeholders in one line
print(f"Summary: {name} ({age} y/o), Messages: {messages}, Tasks Done: {tasks_completed}/{tasks_total}")
