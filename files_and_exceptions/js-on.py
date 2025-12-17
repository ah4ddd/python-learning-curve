import json

player = {
    "name": "Ahad",
    "level": 25,
    "health": 100,
    "mana": 80,
    "inventory": ["sword", "potion", "shield"],
    "gold": 1500,
    "position": {"x": 100, "y": 250}
}

with open("savegame.json", "w") as f:
    json.dump(player, f, indent=4)

print("✅ Game saved!")
