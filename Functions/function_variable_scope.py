players = ["Ahad", "Alice"]
scores = [0, 0]

def play_round(player_index, points):
    round_points = points
    print(f"{players[player_index]} scored {round_points} points this round!")

    scores[player_index] += round_points

def show_leaderboard():
    print("\nLeaderboard:")
    for i in range(len(players)):
        print(f"{players[i]}: {scores[i]} points")

play_round(0, 10)
play_round(1, 15)
play_round(0, 5)

show_leaderboard()
