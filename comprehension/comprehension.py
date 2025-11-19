films = [
    ("Mirror", "Andrei Tarkovsky", 1975, 10),
    ("Memories of Murder", "Bong Joon-ho", 2003, 9),
    ("In the Mood for Love", "Wong Kar Wai", 2000, 10),
    ("Stalker", "Andrei Tarkovsky", 1979, 9),
    ("Paris Texas", "Wim Wenders", 1984, 9.5)
]

cinema = [f for f in films]
titles = [f[0] for f in films]
directors = {f[1] for f in films}
years = {f[2] for f in films}
rating_map = {title: rating for title, _, _, rating in films}
high_rated = [f for f in films if f[3] >= 9.5]
initials = [director.split()[0][0] for _, director, _, _ in films]
flat_data = [item for movie in films for item in movie]
rating_pairs = ((title, rating) for title, _, _, rating in films)

print(f"Films : {cinema}\n")
print(f"Titles: {titles}\n")
print(f"Directors:, {directors}")
print(f"Year : {years}\n")
print(f"Title → Rating:, {rating_map}\n")
print(f"Masterpieces: {high_rated}\n")
print(f"Director Initials: {initials}\n")
print(f"Flattened Data: {flat_data}\n")
print(f"Generator Output: {list(rating_pairs)}\n")
