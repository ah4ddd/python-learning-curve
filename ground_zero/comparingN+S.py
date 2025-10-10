# ------------------------------
# VARIABLES
# ------------------------------
user_name = "Ahad"
friend_name = "Zara"

user_age = 20
friend_age = 25

# ------------------------------
# STRING COMPARISONS
# ------------------------------
print("=== String Comparisons ===")
# Check equality
same_name = user_name == friend_name
print(f"Do you and your friend have the same name? {same_name}")

# Check inequality
different_name = user_name != friend_name
print(f"Are your names different? {different_name}")

# Alphabetical order
comes_first = user_name < friend_name
print(f"Does your name come before your friend's alphabetically? {comes_first}")

# ------------------------------
# NUMBER COMPARISONS
# ------------------------------
print("\n=== Number Comparisons ===")
# Equality
age_equal = user_age == friend_age
print(f"Are you and your friend the same age? {age_equal}")

# Inequality
age_not_equal = user_age != friend_age
print(f"Are you different in age? {age_not_equal}")

# Greater / Less than
older = user_age > friend_age
younger = user_age < friend_age
print(f"Are you older than your friend? {older}")
print(f"Are you younger than your friend? {younger}")

# Greater or equal / Less or equal
age_check1 = user_age >= 20
age_check2 = friend_age <= 25
print(f"Are you at least 20? {age_check1}")
print(f"Is your friend at most 25? {age_check2}")

# ------------------------------
# COMBINING LOGIC
# ------------------------------
print("\n=== Combining Comparisons ===")
# Are you older than your friend AND your name comes first alphabetically?
combined_check1 = (user_age > friend_age) and (user_name < friend_name)
print(f"Older and name comes first? {combined_check1}")

# Are you younger than friend OR your name comes first alphabetically?
combined_check2 = (user_age < friend_age) or (user_name < friend_name)
print(f"Younger or name comes first? {combined_check2}")

# NOT example
not_same_name = not (user_name == friend_name)
print(f"Not the same name? {not_same_name}")
