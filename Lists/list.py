favorite_films = ["city of god", "in the mood for love", "incendies", "come and see", "paris texas"]

favorite_films.append("la haine")

favorite_films[5] = "stalker"

favorite_films.append("the 400 blows")

favorite_films.insert(2, "mulholland Drive")

favorite_films.remove("incendies")

favorite_films.pop(3)

removed_film = favorite_films.pop(5)

for film in favorite_films:
    print(film)

print(f"Removed: {removed_film} and {len(favorite_films)} films left.")



