# 1️⃣ Ask for name (string input)
name = input("What's your name? ")

# 2️⃣ Ask for age (numeric input)
age = int(input("How old are you? "))

# 3️⃣ Ask for height (decimal input)
height = float(input("What's your height in meters? "))

# 4️⃣ Ask a yes/no question (store as boolean)
likes_python = input("Do you like Python? (yes/no) ").lower()
likes_python_bool = likes_python == "yes"

# 5️⃣ Ask number of hobbies (numeric input)
num_hobbies = int(input("How many hobbies do you have? "))

# 6️⃣ Display everything nicely using f-strings
print("\n--- Summary ---")
print(f"Name: {name}")
print(f"Age next year: {age + 1}")
print(f"Height in cm: {height * 100}")
print(f"Likes Python? {likes_python_bool}")
print(f"Number of hobbies: {num_hobbies}")
