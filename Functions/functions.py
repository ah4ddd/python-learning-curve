def calculate_savings(income, expenses):
    savings = income - expenses
    return savings

alice_saves = calculate_savings(5000, 3000)
bob_saves = calculate_savings(6000, 4500)
charlie_saves = calculate_savings(4500, 3200)

def greet_user(name):
    print("=" * 30)
    print(f"Hello, {name}!")
    print("Welcome to our app!")
    print("=" * 30)

greet_user("Alice")
greet_user("Bob")
greet_user("Charlie")

print(f"Alice saves: ${alice_saves}")
print(f"Bob saves: ${bob_saves}")
print(f"Charlie saves: ${charlie_saves}")

