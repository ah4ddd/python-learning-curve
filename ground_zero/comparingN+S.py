# User info
user_name = "Ahad"
user_age = 20
user_fruit = "apple"

# Bot info
bot_name = "Lily"
bot_age = 5
bot_fruit = "banana"

# Compare ages
older_than_bot = user_age > bot_age
same_age_as_bot = user_age == bot_age
age_difference = user_age - bot_age

# Compare favorite fruits
same_fruit = user_fruit == bot_fruit
fruit_order = user_fruit < bot_fruit  # alphabetical comparison

# Output results
print(f"Hello {user_name}! I am {bot_name}, your friendly bot.")

# Age comparisons
print(f"Are you older than me? {older_than_bot}")
print(f"Are we the same age? {same_age_as_bot}")
print(f"You are {age_difference} years older than me.")

# Fruit comparisons
print(f"Do we like the same fruit? {same_fruit}")
print(f"Alphabetically, does your fruit come before mine? {fruit_order}")

# Optional fun: combined Boolean logic
print(f"Are you older than me AND do we like the same fruit? {older_than_bot and same_fruit}")
