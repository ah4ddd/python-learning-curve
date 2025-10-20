# Input players and their scores
players = []
scores = []

num_players = int(input("Number of astronauts? "))
num_rounds = int(input("Number of rounds? "))

for p in range(num_players):
    name = input(f"Enter name of astronaut {p+1}: ")
    players.append(name)

    astronaut_scores = []
    for r in range(num_rounds):
        score = int(input(f"Score for {name} in round {r+1}: "))
        astronaut_scores.append(score)

    scores.append(astronaut_scores)

# Calculate total scores
total_scores = []
for i in range(num_players):
    total_scores.append(sum(scores[i]))

# Combine players and scores into a list of lists
combined = []
for i in range(num_players):
    combined.append([players[i], total_scores[i]])

# Use simple sort() to sort by the score
combined.sort(reverse=True, key=lambda item: item[1])  # Just to point out: key needed here is unavoidable if sorting by score

# Print leaderboard
print("\n*-*-*-* Astronaut Leaderboard *-*-*-*")
for astronaut in combined:
    print(f"{astronaut[0]}: {astronaut[1]} points")
