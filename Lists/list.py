life_experience = ["sex", "drugs", "rock n roll", "travel", "adventure", "food", "friends", "family"]

life_experience.append("learning")
life_experience.insert(0, "fun")
life_experience.remove("rock n roll")
life_experience.pop(7)
life_experience[3] = "exploration"
life_experience[2:4] = ["culture", "nature"]
life_experience_sorted = sorted(life_experience)
life_experience.sort(reverse=True)

print(life_experience)
print(life_experience_sorted)
print(life_experience[1:4])
