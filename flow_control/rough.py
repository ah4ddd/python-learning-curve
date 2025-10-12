print ("welcome to rough.py")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
likes_rough = input("Do you like rough code? (yes/no): ").lower() == "yes"
has_time = input("Do you have time to debug? (yes/no): ").lower() == "yes"
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

if age>=18: #level 1
    print(f"\n{name}, you are old enough to handle rough code.")

    if likes_rough:# nest level 2
        print("Great! You seem to enjoy challenges.")

        if has_time:# nest level 3 of level 2
            print("You have time to debug. Let's dive into some rough code!")

            if is_student:#nest level 4 of level 3 of level 2
                print("As a student, this is a great learning opportunity for you.")
            else:#nest level 4 of level 3 of level 2 (sibling of if is_student)
                print("Even if you're not a student, learning is a lifelong journey.")
        else: #nest level 3 of level 2 (sibling of if has_time)
            print("Without time to debug, rough code can be frustrating. Consider starting with simpler code.")

if not likes_rough: #level 1 (independent if)
    print("No worries! Not everyone enjoys rough code.")
if age<18: #level 1 (independent if)
    print(f"Sorry {name}, you might find rough code overwhelming at your age.")
if not has_time: #level 1   (independent if)
    print("Remember, debugging is a crucial skill in programming.")
if not is_student: #level 1  (independent if)
    print("Consider taking some courses to improve your coding skills.")

print("\nThanks for visiting the Rough Code Experience!")

