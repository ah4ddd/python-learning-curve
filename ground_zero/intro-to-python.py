# --- Welcome & Name ---
name = input("Hello! What is your name? ")
print(f"Nice to meet you, {name}!")

# --- Age & Calculation ---
age = int(input("How old are you? "))
bot_age = 3
age_difference = age - bot_age
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")

# --- Favorite Things ---
color = input("What's your favorite color? ")
food = input("What's your favorite food? ")
print(f"Wow, {color} and {food} sound awesome!")

# --- Hobbies & Boolean ---
num_hobbies = int(input("How many hobbies do you have? "))
likes_python = input("Do you like Python? (yes/no) ").lower()
likes_python_bool = likes_python == "yes"

print(f"So you have {num_hobbies} hobbies, and liking Python? {likes_python_bool}")

# --- Numeric Comparison ---
high_score = int(input("Enter your high score in a game: "))
target_score = 100
print(f"Did you beat the target score of {target_score}? {high_score >= target_score}")

# --- String Comparison ---
fav_city = input("What's your favorite city? ")
my_city = "Tokyo"
print(f"Is your favorite city different from mine? {fav_city != my_city}")

# --- Expression & Calculation ---
hours_studied = float(input("How many hours did you study today? "))
hours_needed = 5
more_hours_needed = hours_needed - hours_studied
print(f"You need {more_hours_needed} more hours to reach {hours_needed} hours goal.")

# --- Final Summary using f-string ---
print("\n--- Summary ---")
print(f"Name: {name}")
print(f"Age: {age}, Age difference with bot: {age_difference}")
print(f"Favorite color: {color}, Favorite food: {food}")
print(f"Number of hobbies: {num_hobbies}, Likes Python? {likes_python_bool}")
print(f"High score: {high_score} (beat target? {high_score >= target_score})")
print(f"Favorite city: {fav_city} (different from bot? {fav_city != my_city})")
print(f"Hours studied today: {hours_studied}, More hours needed: {more_hours_needed}")
