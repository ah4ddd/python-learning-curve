songs = ("Creep", "Smells Like Teen Spirit", "Paranoid", "Fade to Black", "Karma Police")
print(songs)

print("My first favorite song is:", songs[0])
print("My last favorite song is:", songs[-1])

print("\n🎵 My Favorite Songs:")
for song in songs:
    print("-", song)

if "Paranoid" in songs:
    print("\n✅ Paranoid is one of my favorite songs!")
else:
    print("\n❌ Not in the list.")

playlist = (
    ("Creep", "Radiohead", 1993),
    ("Smells Like Teen Spirit", "Nirvana", 1991),
    ("Paranoid", "Black Sabbath", 1970),
    ("Fade to Black", "Metallica", 1984)
)

print("\n🎧 My Playlist:")
for song, artist, year in playlist:
 print("\n🎧 My Playlist:")

for song, artist, year in playlist:
    print(f"{song} — by {artist} in {year}")

search_artist = "Radiohead"

print(f"\n🔎 Songs by {search_artist}:")
for song, artist, year in playlist:
    if artist == search_artist:
        print("-", song)
