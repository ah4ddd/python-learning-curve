players = []
scores = []

num_players = int(input("Number of players? "))
num_rounds = int(input("Number of rounds? "))

for p in range(num_players):
    name = input(f"Enter name of player {p+1}: ")
    players.append(name)

    player_scores = []
    for r in range(num_rounds):
        score = int(input(f"Score for {name} in round {r+1}: "))
        player_scores.append(score)

    scores.append(player_scores)

max_score = -float('inf')
min_score = float('inf')

max_player = ""
min_player = ""

max_round = 0
min_round = 0

for i in range(num_players):
    for j in range(num_rounds):
        score = scores[i][j]

        if score > max_score:
            max_score = score
            max_player = players[i]
            max_round = j+1

        if score < min_score:
            min_score = score
            min_player = players[i]
            min_round = j+1

print(f"\nOverall Highest Score: {max_score} by {max_player} in Round {max_round}")
print(f"Overall Lowest Score: {min_score} by {min_player} in Round {min_round}")

print("\nTop performer per round:")

for r in range(num_rounds):
    top_score = -float('inf')
    top_player = ""

    for i in range(num_players):
        if scores[i][r] > top_score:
            top_score = scores[i][r]
            top_player = players[i]

    print(f"Round {r+1}: {top_player} with {top_score} points")
