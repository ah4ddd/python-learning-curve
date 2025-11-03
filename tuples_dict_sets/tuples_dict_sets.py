def check_password_strength(password):
    MIN_LENGTH = 8
    failed_rules = []

    if len(password) < MIN_LENGTH:
        failed_rules.append(f"❌ Must be at least {MIN_LENGTH} characters long.")

    if not any(c.isupper() for c in password):
        failed_rules.append("❌ Must contain at least one uppercase letter.")

    if not any(c.islower() for c in password):
        failed_rules.append("❌ Must contain at least one lowercase letter.")

    if not any(c.isdigit() for c in password):
        failed_rules.append("❌ Must contain at least one number.")

    special_chars = "!@#$%^&*()-_+="
    if not any(c in special_chars for c in password):
        failed_rules.append("⚠️ Recommendation: Add a special character (!@#$).")

    if not failed_rules:
        return True, "✅ Password is strong and meets all requirements!"
    else:
        return False, failed_rules


def main():
    while True:
        print("\n" + "="*40)
        print("🔒 PASSWORD STRENGTH CHECKER")
        print("="*40)

        user_password = input("Enter password to check (or type 'quit' to exit): ")

        if user_password.lower() == 'quit':
            print("👋 Exiting the checker. Goodbye!")
            break

        if not user_password:
            print("⚠️ Please enter a password to check.")
            continue

        is_strong, result = check_password_strength(user_password)

        if is_strong:
            print(result)
        else:
            print("Password Status: 🔴 WEAK or MEH. Reasons:")
            for rule in result:
                print(f"  {rule}")

if __name__ == "__main__":
    main()
