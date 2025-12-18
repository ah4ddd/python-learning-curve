import json

HISTORY_FILE = "history.json"


def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_history(history):
    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f, indent=4)
    except Exception as e:
        print(f"⚠️ Failed to save history: {e}")


def calculate(user):
    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            try:
                result = a / b
            except ZeroDivisionError:
                print("❌ Cannot divide by zero!")
                return
        else:
            print("❌ Invalid operator!")
            return

        print(f"✅ Result: {a} {operator} {b} = {result}")

        history = load_history()

        entry = {
            "user": user,
            "a": a,
            "operator": operator,
            "b": b,
            "result": result
        }

        history.append(entry)
        save_history(history)

    except ValueError:
        print("❌ Please enter valid numbers.")


def show_history():
    history = load_history()

    if not history:
        print("📭 No history yet.")
        return

    print("\n📜 CALCULATION HISTORY")
    print("=" * 40)

    for i, entry in enumerate(history, start=1):
        print(
            f"{i}. [{entry['user']}] "
            f"{entry['a']} {entry['operator']} {entry['b']} = {entry['result']}"
        )

    print()


def main():
    user = input("👤 Enter your name: ").strip() or "Anonymous"

    while True:
        print("\n🔢 CALCULATOR")
        print("=" * 30)
        print("1. Calculate")
        print("2. Show history")
        print("3. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            calculate(user)
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("👋 Bye.")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
