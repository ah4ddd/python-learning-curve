# Album structure:
# (album_name, artist, year, [list of songs])

music_library = [
    ("Dark Side of the Moon", "Pink Floyd", 1973,
     ["Speak to Me", "Breathe", "Time", "Money"]),

    ("Thriller", "Michael Jackson", 1982,
     ["Wanna Be Startin' Somethin'", "Thriller", "Beat It"]),

    ("OK Computer", "Radiohead", 1997,
     ["Paranoid Android", "Karma Police", "No Surprises"])
]

# Function to add a song to an album:
def add_song_to_album(library, album_name, new_song):
    for album in library:
        if album[0] == album_name:
            album[3].insert(0, new_song)  # album[3] is the song list
            print(f"✅ Added '{new_song}' to {album_name}")
            return
    print(f"❌ Album '{album_name}' not found")

# Add a song:
add_song_to_album(music_library, "Thriller", "Billie Jean")

# Check it:
for album in music_library:
    if album[0] == "Thriller":
        print(album[3])
# ['Wanna Be Startin' Somethin'', 'Thriller', 'Beat It', 'Billie Jean']
