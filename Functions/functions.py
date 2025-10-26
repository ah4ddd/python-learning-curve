def get_all_recommendations(mood):
    """Return ALL movies for a mood"""
    recommendations = []

    if mood == "reflective":
        recommendations = [
            "The Seventh Seal (1957)",
            "Persona (1966)",
            "Eraserhead (1977)",
            "Wings of Desire (1987)"
        ]
    elif mood == "curious":
        recommendations = [
            "Baraka (1992)",
            "Stalker (1979)",
            "Tokyo Story (1953)",
            "Andrei Rublev (1966)"
        ]
    elif mood == "dreamy":
        recommendations = [
            "Pan's Labyrinth (2006)",
            "Spirited Away (2001)",
            "The Holy Mountain (1973)"
        ]

    return recommendations

def filter_by_decade(movies, decade):
    """Filter movies from a specific decade"""
    filtered = []
    for movie in movies:
        if f"({decade}" in movie:  # Check if decade in title
            filtered.append(movie)
    return filtered

# Use it:
reflective_films = get_all_recommendations("reflective")
print("All reflective films:")
for film in reflective_films:
    print(f"  • {film}")

# Filter to 1960s only:
sixties_films = filter_by_decade(reflective_films, "196")
print("\n1960s reflective films:")
for film in sixties_films:
    print(f"  • {film}")
