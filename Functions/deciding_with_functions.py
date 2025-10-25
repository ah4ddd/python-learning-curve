def recommend_art_movie(mood, genre):

    if mood == "reflective":
        if genre == "drama":
            return "The Seventh Seal (1957)"
        elif genre == "psychological":
            return "Persona (1966)"
        elif genre == "experimental":
            return "Eraserhead (1977)"
        else:
            return "Wings of Desire (1987)"

    elif mood == "curious":
        if genre == "documentary":
            return "Baraka (1992)"
        elif genre == "surreal":
            return "Stalker (1979)"
        elif genre == "drama":
            return "Tokyo Story (1953)"
        else:
            return "Andrei Rublev (1966)"

    elif mood == "dreamy":
        if genre == "fantasy":
            return "Pan's Labyrinth (2006)"
        elif genre == "animation":
            return "Spirited Away (2013)"
        else:
            return "The Holy Mountain (1973)"
    else:
        return "8½ (1963)"

my_mood = input("Your mood (reflective/curious/dreamy/other): ")
my_genre = input("Preferred genre (drama/psychological/experimental/documentary/surreal/fantasy/animation): ")

movie_choice = recommend_art_movie(my_mood, my_genre)
print("\nArt film recommendation for you:", movie_choice)
