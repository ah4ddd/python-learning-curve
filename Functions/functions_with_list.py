def add_artwork(collection, title, artist, price):
    collection.append([title, artist, price])
    print(f"🎨 Added '{title}' by {artist} for ${price}")

def display_artworks(collection):
    print("\n🖼️ Current Gallery Collection:")
    for art in collection:
        print(f" - '{art[0]}' by {art[1]} (${art[2]})")

def find_most_expensive(collection):
    most_expensive = max(collection, key=lambda x: x[2])
    print(f"\n💸 Most Expensive Artwork:")
    print(f"'{most_expensive[0]}' by {most_expensive[1]} - ${most_expensive[2]}")

def remove_artwork(collection, title):
    for art in collection:
        if art[0].lower() == title.lower():
            collection.remove(art)
            print(f"🗑 Removed '{title}' (sold!)")
            return
    print(f"⚠️ Artwork '{title}' not found.")

art_collection = [
    ["Starry Night", "Vincent van Gogh", 1200000],
    ["The Persistence of Memory", "Salvador Dalí", 950000],
    ["Girl with a Pearl Earring", "Johannes Vermeer", 870000],
]

display_artworks(art_collection)

add_artwork(art_collection, "The Scream", "Edvard Munch", 1150000)
add_artwork(art_collection, "Guernica", "Pablo Picasso", 2000000)

display_artworks(art_collection)

find_most_expensive(art_collection)

remove_artwork(art_collection, "Girl with a Pearl Earring")

display_artworks(art_collection)
