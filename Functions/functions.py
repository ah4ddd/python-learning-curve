artworks = [
    {"title": "Starry Night", "artist": "Vincent van Gogh", "style": "Post-Impressionism", "mood": "Melancholic", "rating": 9.8},
    {"title": "The Persistence of Memory", "artist": "Salvador Dalí", "style": "Surrealism", "mood": "Dreamlike", "rating": 9.6},
    {"title": "Guernica", "artist": "Pablo Picasso", "style": "Cubism", "mood": "Tragic", "rating": 9.5},
    {"title": "The Scream", "artist": "Edvard Munch", "style": "Expressionism", "mood": "Anxious", "rating": 9.3},
    {"title": "The Two Fridas", "artist": "Frida Kahlo", "style": "Surrealism", "mood": "Emotional", "rating": 9.1},
    {"title": "Girl with a Pearl Earring", "artist": "Johannes Vermeer", "style": "Baroque", "mood": "Calm", "rating": 8.9},
    {"title": "The Birth of Venus", "artist": "Sandro Botticelli", "style": "Renaissance", "mood": "Romantic", "rating": 8.7},
    {"title": "Composition VII", "artist": "Wassily Kandinsky", "style": "Abstract", "mood": "Chaotic", "rating": 9.0}
]

def display_artworks(art_list):
    print("\n🎨 Artworks in The Eternal Gallery:\n")
    for art in art_list:
        print(f"'{art['title']}' — {art['artist']} | {art['style']} | Mood: {art['mood']} | Rating: {art['rating']}⭐")

def add_artwork(art_list, title, artist, style, mood, rating):
    new_art = {"title": title, "artist": artist, "style": style, "mood": mood, "rating": rating}
    art_list.append(new_art)
    print(f"\n✅ '{title}' by {artist} added to the eternal collection.")

def filter_by_mood(art_list, mood):
    result = []
    for art in art_list:
        if art["mood"].lower() == mood.lower():
            result.append(art)
    return result

def update_rating(art_list, title, new_rating):
    for art in art_list:
        if art["title"].lower() == title.lower():
            art["rating"] = new_rating
            print(f"\n⭐ Updated: '{title}' now rated {new_rating}/10")
            return
    print(f"\n❌ Artwork '{title}' not found in the archives.")

def get_top_artwork(art_list):
    top = max(art_list, key=lambda art: art["rating"])
    return top

def run_gallery():
    while True:
        print("\n===== 🎭 The Eternal Gallery Menu =====")
        print("1. View all artworks")
        print("2. Add a new artwork")
        print("3. Filter artworks by mood")
        print("4. Update artwork rating")
        print("5. Show top-rated artwork")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_artworks(artworks)

        elif choice == "2":
            title = input("Title: ")
            artist = input("Artist: ")
            style = input("Style: ")
            mood = input("Mood: ")
            rating = float(input("Rating (out of 10): "))
            add_artwork(artworks, title, artist, style, mood, rating)

        elif choice == "3":
            mood = input("Enter mood to filter (e.g. 'Melancholic', 'Romantic'): ")
            results = filter_by_mood(artworks, mood)
            if results:
                display_artworks(results)
            else:
                print("\n❌ No artworks found matching that mood.")

        elif choice == "4":
            title = input("Enter artwork title to update rating: ")
            new_rating = float(input("New rating (out of 10): "))
            update_rating(artworks, title, new_rating)

        elif choice == "5":
            top = get_top_artwork(artworks)
            print(f"\n🏆 Top Artwork: '{top['title']}' — {top['artist']} ({top['style']}) with {top['rating']}⭐")

        elif choice == "6":
            print("\n🖼 Thank you for curating with The Eternal Gallery. Farewell.")
            break

        else:
            print("\n❌ Invalid choice. Try again.")

run_gallery()
