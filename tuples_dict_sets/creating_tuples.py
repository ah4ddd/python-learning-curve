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
    ("Creep", "Radiohead"),
    ("Smells Like Teen Spirit", "Nirvana"),
    ("Paranoid", "Black Sabbath"),
    ("Fade to Black", "Metallica"),
    ("Karma Police", "Radiohead")
)

print("\n🎧 My Playlist:")
for song, artist in playlist:
 print("\n🎧 My Playlist:")
for song, artist in playlist:
    print(f"{song} — by {artist}")

search_artist = "Radiohead"

print(f"\n🔎 Songs by {search_artist}:")
for song, artist in playlist:
    if artist == search_artist:
        print("-", song)
