def display_menu():
    print("\n" + "="*40)
    print("🎬 MOVIE COLLECTION MANAGER")
    print("="*40)
    print("1. Add movie")
    print("2. Show all movies")
    print("3. Search movie")
    print("4. Remove movie")
    print("5. Show statistics")
    print("6. Exit")
    print("="*40)

def get_user_choice():
    while True:
        choice = input("\nEnter choice (1-6): ")
        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice
        else:
            print("❌ Invalid choice! Try again.")

def add_movie(collection):
    print("\n➕ ADD NEW MOVIE")
    title = input("Movie title: ")
    director = input("Director: ")

    while True:
        year = input("Year: ")
        if year.isdigit() and 1900 <= int(year) <= 2025:
            year = int(year)
            break
        print("Invalid year!")

    while True:
        rating = input("Rating (1-10): ")
        if rating.isdigit() and 1 <= int(rating) <= 10:
            rating = int(rating)
            break
        print("Invalid rating!")

    movie = [title, director, year, rating]
    collection.append(movie)

    print(f"✅ Added '{title}' to collection!")

def show_all_movies(collection):
    if len(collection) == 0:
        print("\n📭 No movies in collection yet!")
        return

    print("\n🎬 YOUR MOVIE COLLECTION:")
    print("="*60)

    for i, movie in enumerate(collection):
        title = movie[0]
        director = movie[1]
        year = movie[2]
        rating = movie[3]

        print(f"{i+1}. {title} ({year})")
        print(f"   Director: {director}")
        print(f"   Rating: {'⭐'*rating} ({rating}/10)")
        print("-"*60)

def search_movie(collection, search_term):
    results = []

    for movie in collection:
        title = movie[0]
        if search_term.lower() in title.lower():
            results.append(movie)

    return results

def remove_movie(collection, title):
    for movie in collection:
        if movie[0].lower() == title.lower():
            collection.remove(movie)
            print(f"🗑️ Removed '{title}' from collection")
            return True

    print(f"❌ Movie '{title}' not found!")
    return False

def calculate_statistics(collection):
    if len(collection) == 0:
        print("\n📊 No statistics yet - collection is empty!")
        return

    print("\n📊 COLLECTION STATISTICS:")
    print("="*40)

    total = len(collection)
    print(f"Total movies: {total}")

    ratings = []
    for movie in collection:
        ratings.append(movie[3])

    avg_rating = sum(ratings) / len(ratings)
    print(f"Average rating: {avg_rating:.2f}/10")

    highest_rating = max(ratings)
    for movie in collection:
        if movie[3] == highest_rating:
            print(f"Highest rated: {movie[0]} ({highest_rating}/10)")
            break

    lowest_rating = min(ratings)
    for movie in collection:
        if movie[3] == lowest_rating:
            print(f"Lowest rated: {movie[0]} ({lowest_rating}/10)")
            break

    print("="*40)

def main():

    collection = []

    print("🎬 Welcome to Movie Collection Manager!")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            add_movie(collection)

        elif choice == "2":
            show_all_movies(collection)

        elif choice == "3":
            term = input("\nSearch for: ")
            results = search_movie(collection, term)
            if len(results) > 0:
                print(f"\n🔍 Found {len(results)} movie(s):")
                show_all_movies(results)
            else:
                print(f"❌ No movies found matching '{term}'")

        elif choice == "4":
            title = input("\nMovie title to remove: ")
            remove_movie(collection, title)

        elif choice == "5":
            calculate_statistics(collection)

        elif choice == "6":
            print("\n👋 Thanks for using Movie Manager!")
            break

main()
