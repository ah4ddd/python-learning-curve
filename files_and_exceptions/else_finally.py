try:
    number = int(input("Enter number: "))
    print(f"Number: {number}")
except ValueError:
    print("❌ Invalid input!")
finally:
    print("🧹 Cleanup: This ALWAYS runs!")
