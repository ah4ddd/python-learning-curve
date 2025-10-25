def fight(player1, attack1, defense1, health1,
          player2, attack2, defense2, health2):

    print(f"\n⚔️ BATTLE START: {player1} vs {player2} ⚔️")

    power1 = attack1 * 2 + defense1 * 1.5 + health1 * 0.8
    power2 = attack2 * 2 + defense2 * 1.5 + health2 * 0.8

    print(f"{player1}'s total power: {power1}")
    print(f"{player2}'s total power: {power2}")

    if power1 > power2:
        print(f"🔥 {player1} wins the fight!")
        return player1
    elif power2 > power1:
        print(f"🔥 {player2} wins the fight!")
        return player2
    else:
        print("🤝 It's a draw!")
        return "Draw"

winner = fight("Ahad", 80, 60, 100,
                "Drago", 75, 70, 95)

print(f"\n🏆 The winner is: {winner}!")
