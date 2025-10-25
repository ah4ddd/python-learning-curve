players = ["Ahad", "Alice"]
scores = [0, 0]

def play_round(player_index, points):
    if points >= 20:
        bonus = 5
        points += bonus
        print(f"🎉 Bonus! +{bonus} points for amazing performance!")

    scores[player_index] += points
    print(f"{players[player_index]} scored {points} points this round!")

def get_winner():
    if scores[0] > scores[1]:
        return players[0]
    elif scores[1] > scores[0]:
        return players[1]
    else:
        return "It's a tie!"

def show_leaderboard():
    print("\n📊 Leaderboard:")
    for i in range(len(players)):
        print(f"{players[i]}: {scores[i]} points")

    winner = get_winner()
    print(f"\n🏆 Winner: {winner}")

play_round(0, 10)
play_round(1, 25)
play_round(0, 15)

show_leaderboard()
