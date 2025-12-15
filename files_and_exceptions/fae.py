def save_score(player_name, score):
    """Save a high score to file."""
    with open("highscores.txt", "a") as f:
        f.write(f"{player_name}:{score}\n")
    print(f"✅ Saved {player_name}'s score: {score}")

def load_scores():
    """Load all high scores from file."""
    try:
        with open("highscores.txt", "r") as f:
            lines = f.readlines()

        scores = []
        for line in lines:
            line = line.strip()
            if line:
                name, score = line.split(":")
                scores.append({"name": name, "score": int(score)})

        return scores
    except FileNotFoundError:
        return []

def display_top_scores():
    """Display top 5 scores."""
    scores = load_scores()

    if not scores:
        print("No scores yet!")
        return

    # Sort by score (highest first)
    scores.sort(key=lambda x: x["score"], reverse=True)

    print("\n🏆 TOP 5 HIGH SCORES 🏆")
    for i, entry in enumerate(scores[:5], 1):
        print(f"{i}. {entry['name']}: {entry['score']} points")

# Simulate game sessions
save_score("Ahad", 1500)
save_score("Mia", 1800)
save_score("Sara", 1200)
save_score("Zexo", 1650)
save_score("Ahad", 2000)  # Ahad plays again!

# Display leaderboard
display_top_scores()

x = (lambda x: x + 1)

print(x(1))
