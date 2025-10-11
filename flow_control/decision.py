print("Welcome to Python Club Rewards System!\n")

# User input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"
vip_pass = input("Do you have a VIP pass? (yes/no): ").lower() == "yes"
loyalty_points = int(input("Enter your loyalty points: "))

# Decision making
if age >= 18 and has_id:
    print(f"\n{name}, you can enter the club!")

    if vip_pass and loyalty_points >= 100:
        print("Wow! VIP pass + loyalty points >= 100! You get free drinks!")
    elif vip_pass or loyalty_points >= 100:
        print("Nice! Either VIP or enough loyalty points. You get a free snack!")
    else:
        print("Regular entry granted. Enjoy the club!")

elif age >= 18 and not has_id:
    print(f"\n{name}, you are adult but need an ID to enter.")

else:
    print(f"\n{name}, sorry, you are underage and cannot enter.")

# Extra decision: special greeting
if not has_id:
    print("Remember to bring your ID next time!")

if age < 25 and loyalty_points > 50:
    print("Young and loyal! You might get bonus points next visit.")

print("\nThank you for using the Python Club Rewards System!")
