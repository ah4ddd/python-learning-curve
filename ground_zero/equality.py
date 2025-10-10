# Smart PIN & Score Checker 🔐

# Stored PIN and user-entered PIN
saved_pin = 4321
entered_pin = int(input("Enter your 4-digit PIN: "))

# Check if the PINs match
pin_match = saved_pin == entered_pin
print("PIN match:", pin_match)

# If correct PIN
if pin_match:
    print("✅ Access granted! Welcome back.")

    # Let's check some score comparisons
    score_one = int(input("Enter your first score: "))
    score_two = int(input("Enter your second score: "))

    print("Are both scores equal?", score_one == score_two)
    print("Are the scores different?", score_one != score_two)
    print("Is the first score higher?", score_one > score_two)
    print("Is the first score lower?", score_one < score_two)
    print("Is the first score at least equal?", score_one >= score_two)
    print("Is the second score at least equal?", score_two >= score_one)

else:
    print("❌ Incorrect PIN. Access denied.")
