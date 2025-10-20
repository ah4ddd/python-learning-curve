# Astronaut mission sorting project

astronauts = ["Ahad", "Leo", "Nova", "Rhea", "Kai"]
scores = [92, 78, 88, 95, 81]

# Combine both lists
combined = list(zip(astronauts, scores))

# Sort by score (the 2nd value in each pair) in descending order
combined.sort(key=lambda x: x[1], reverse=True)

# Display sorted results
print("🚀 Astronaut Mission Rankings:")
for rank, (name, score) in enumerate(combined, start=1):
    print(f"{rank}. {name} — {score} points")
