players = []
scores = []

num_players = int(input("How many players? "))

for players_score in range(num_players):
    name = input("Enter player name: ")
    score = int(input(f"Enter score for {name}: "))

    players.append(name)
    scores.append(score)

# Find highest and lowest score
max_score = max(scores)
min_score = min(scores)

# Find who has these scores
winner = players[scores.index(max_score)]
loser = players[scores.index(min_score)]

print(f"\nWinner: {winner} with {max_score} points")
print(f"Loser: {loser} with {min_score} points")
