# User profile
profile = {
    "name": "Ahad",
    "age": 20,
    "location": "India",
    "language": "Python",
    "level": "Intermediate"
}

# Save to file
with open("profile.txt", "w") as f:
    for key, value in profile.items():
        f.write(f"{key}: {value}\n")

print("✅ Profile saved!")

# Display the file
with open("profile.txt", "r") as f:
    print("\n👤 Profile:")
    print(f.read())
