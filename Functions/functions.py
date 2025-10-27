# This is our "database" - a list that will hold all films
film_journal = []

def display_header(text):

    print("\n" + "=" * 50)
    print(f"🎬 {text.upper()} 🎬".center(50))
    print("=" * 50)

def display_menu():
    """
    Shows the main menu options

    What it does: Prints all available actions user can take
    Why: Menu is shown repeatedly, so function prevents repetition
    Returns: Nothing (just displays)
    """
    display_header("Main Menu")
    print("1. 📝 Log a new film")
    print("2. 🎞️  View all films")
    print("3. 🔍 Search films")
    print("4. 📊 View statistics")
    print("5. 🎯 Check watching goals")
    print("6. 💭 Read random film note")
    print("7. 🚪 Exit journal")
    print("=" * 50)

def get_valid_choice(min_choice, max_choice):
    """
    Gets a valid menu choice from user

    Parameters:
        min_choice: Lowest valid number (e.g., 1)
        max_choice: Highest valid number (e.g., 7)

    What it does: Keeps asking until user enters valid number
    Why: Validation logic in ONE place, reusable
    Returns: Valid choice as string

    Uses: While loop (keep asking), conditions (validation)
    """
    while True:  # Infinite loop until we get valid input
        choice = input(f"\nEnter choice ({min_choice}-{max_choice}): ")

        # Check if it's a digit AND in valid range
        if choice.isdigit() and min_choice <= int(choice) <= max_choice:
            return choice  # Valid! Return immediately
        else:
            print(f"❌ Invalid! Please enter {min_choice}-{max_choice}")

def get_rating():
    """
    Gets valid film rating from user (1-10)

    What it does: Asks for rating, validates it's 1-10
    Why: Rating validation is complex enough for its own function
    Returns: Integer rating between 1-10

    Uses: While loop, conditions, return value
    """
    while True:
        rating = input("Rating (1-10): ")

        if rating.isdigit():
            rating = int(rating)
            if 1 <= rating <= 10:
                return rating  # Valid rating!

        print("❌ Please enter a number between 1 and 10")

def get_mood():
    """
    Gets user's mood when watching film

    What it does: Shows mood options and validates choice
    Why: Moods are specific choices, need validation
    Returns: Mood as string

    Uses: List of options, loop, conditions
    """
    moods = ["Reflective", "Curious", "Dreamy", "Melancholic", "Energized", "Other"]

    print("\nWhat mood were you in?")
    for i, mood in enumerate(moods):
        print(f"  {i+1}. {mood}")

    while True:
        choice = input(f"Choose mood (1-{len(moods)}): ")

        if choice.isdigit() and 1 <= int(choice) <= len(moods):
            return moods[int(choice) - 1]  # Return the mood string

        print("❌ Invalid choice!")

def add_film(journal):
    """
    Logs a new film entry to the journal

    Parameters:
        journal: The list holding all films (passed by reference)

    What it does:
        1. Collects all film information
        2. Validates each piece
        3. Creates film entry
        4. Adds to journal

    Why: Adding a film is complex, needs dedicated function
    Returns: Nothing (modifies journal directly)

    Uses: Multiple parameters, validation functions, lists, scope
    """
    display_header("Log New Film")

    # Collect basic info (strings, no validation needed)
    title = input("Film title: ")
    director = input("Director: ")

    # Year with validation
    while True:
        year = input("Year: ")
        if year.isdigit() and 1888 <= int(year) <= 2025:  # Cinema started ~1888
            year = int(year)
            break
        print("❌ Invalid year!")

    # Use our validation functions!
    rating = get_rating()  # Function call!
    mood = get_mood()      # Function call!

    # Genre selection
    genres = ["Drama", "Documentary", "Experimental", "Horror", "Comedy", "Other"]
    print("\nGenre:")
    for i, genre in enumerate(genres):
        print(f"  {i+1}. {genre}")

    while True:
        choice = input(f"Choose genre (1-{len(genres)}): ")
        if choice.isdigit() and 1 <= int(choice) <= len(genres):
            genre = genres[int(choice) - 1]
            break
        print("❌ Invalid!")

    # Personal notes (optional)
    notes = input("Personal notes (or press Enter to skip): ")
    if notes == "":
        notes = "No notes"

    # Create the film entry as a list
    film = [title, director, year, rating, mood, genre, notes]

    # Add to journal (modifies the original list!)
    journal.append(film)

    print(f"\n✅ '{title}' added to your journal!")

def view_all_films(journal):
    """
    Displays all films in the journal

    Parameters:
        journal: List of all films

    What it does: Loops through journal and displays each beautifully
    Why: Displaying needs formatting, keep it in one function
    Returns: Nothing (just displays)

    Uses: Loops, lists, conditions (empty check)
    """
    if len(journal) == 0:
        print("\n📭 Your journal is empty! Watch some films!")
        return  # Exit early if empty

    display_header(f"Your Film Journal ({len(journal)} films)")

    # Loop through each film with index
    for i, film in enumerate(journal):
        # Unpack the film list for readability
        title = film[0]
        director = film[1]
        year = film[2]
        rating = film[3]
        mood = film[4]
        genre = film[5]
        notes = film[6]

        # Display formatted
        print(f"\n{i+1}. {title} ({year})")
        print(f"   🎬 Director: {director}")
        print(f"   🎭 Genre: {genre}")
        print(f"   {'⭐' * rating} ({rating}/10)")
        print(f"   💭 Mood: {mood}")
        print(f"   📝 Notes: {notes}")
        print("-" * 50)

def search_by_mood(journal, target_mood):
    """
    Finds all films watched in a specific mood

    Parameters:
        journal: List of all films
        target_mood: The mood to search for

    What it does: Filters journal by mood
    Why: Searching is a specific task, separate function
    Returns: NEW list with matching films

    Uses: Loops, conditions, lists, return value
    """
    results = []  # Start with empty list

    # Loop through each film
    for film in journal:
        film_mood = film[4]  # Mood is at index 4

        # Case-insensitive comparison
        if target_mood.lower() in film_mood.lower():
            results.append(film)  # Add to results

    return results  # Give back the matches


def search_films(journal):
    """
    Main search interface - lets user choose how to search

    Parameters:
        journal: List of all films

    What it does: Provides search options and shows results
    Why: Coordinate searching, display results
    Returns: Nothing (displays results)

    Uses: Functions calling functions, conditions, loops
    """
    if len(journal) == 0:
        print("\n📭 Nothing to search! Journal is empty.")
        return

    display_header("Search Films")
    print("1. By mood")
    print("2. By director")
    print("3. By minimum rating")

    choice = get_valid_choice(1, 3)  # Reusing validation function!

    if choice == "1":
        mood = input("\nEnter mood to search: ")
        results = search_by_mood(journal, mood)  # Call search function!

        if len(results) > 0:
            print(f"\n🔍 Found {len(results)} film(s) in '{mood}' mood:")
            view_all_films(results)  # Reuse display function!
        else:
            print(f"\n❌ No films found in '{mood}' mood")

    elif choice == "2":
        director = input("\nEnter director name: ")
        results = search_by_director(journal, director) # pyright: ignore[reportUndefinedVariable]

        if len(results) > 0:
            print(f"\n🔍 Found {len(results)} film(s) by {director}:")
            view_all_films(results)
        else:
            print(f"\n❌ No films by '{director}' found")

    elif choice == "3":
        min_rating = get_rating()  # Reuse rating function!
        results = search_by_rating(journal, min_rating) # type: ignore

        if len(results) > 0:
            print(f"\n🔍 Found {len(results)} film(s) rated {min_rating}+:")
            view_all_films(results)
        else:
            print(f"\n❌ No films rated {min_rating}+ found")

def calculate_average_rating(journal):
    """
    Calculate average rating of all films

    Parameters:
        journal: List of films

    What it does: Extracts all ratings, calculates average
    Why: Statistics calculation, separate concern
    Returns: Average as float, or 0 if empty

    Uses: Loops, lists, calculations, return value
    """
    if len(journal) == 0:
        return 0

    ratings = []  # Collect all ratings

    for film in journal:
        ratings.append(film[3])  # Rating is at index 3

    average = sum(ratings) / len(ratings)
    return average

def find_favorite_directors(journal):
    """
    Finds which directors you've watched most

    Parameters:
        journal: List of films

    What it does: Counts films per director, finds top ones
    Why: Complex analysis, needs dedicated function
    Returns: List of [director, count] pairs, sorted

    Uses: Loops, lists, counting, sorting
    """
    if len(journal) == 0:
        return []

    # Count films per director
    director_counts = []

    for film in journal:
        director = film[1]

        # Check if we've seen this director before
        found = False
        for entry in director_counts:
            if entry[0] == director:
                entry[1] += 1  # Increment count
                found = True
                break

        # If new director, add to list
        if not found:
            director_counts.append([director, 1])

    # Sort by count (descending)
    director_counts.sort(key=lambda x: x[1], reverse=True)

    return director_counts

def get_mood_distribution(journal):
    """
    Shows which moods you watch films in most

    Similar to director counting but for moods
    """
    if len(journal) == 0:
        return []

    mood_counts = []

    for film in journal:
        mood = film[4]

        found = False
        for entry in mood_counts:
            if entry[0] == mood:
                entry[1] += 1
                found = True
                break

        if not found:
            mood_counts.append([mood, 1])

    mood_counts.sort(key=lambda x: x[1], reverse=True)
    return mood_counts

def display_statistics(journal):
    """
    Shows comprehensive statistics about viewing habits

    Parameters:
        journal: List of films

    What it does: Calls ALL stat functions, displays results
    Why: Coordinate statistics display
    Returns: Nothing (just displays)

    Uses: Function composition, all previous functions!
    """
    if len(journal) == 0:
        print("\n📊 No statistics yet! Watch some films first!")
        return

    display_header("Your Viewing Statistics")

    # Total films
    total = len(journal)
    print(f"📊 Total films watched: {total}")

    # Average rating
    avg = calculate_average_rating(journal)
    print(f"⭐ Average rating: {avg:.2f}/10")

    # Highest rated
    highest = max(journal, key=lambda x: x[3])
    print(f"🏆 Highest rated: {highest[0]} ({highest[3]}/10)")

    # Favorite directors
    print("\n🎬 Top Directors:")
    directors = find_favorite_directors(journal)
    for i, entry in enumerate(directors[:3]):  # Show top 3
        print(f"   {i+1}. {entry[0]} ({entry[1]} films)")

    # Mood distribution
    print("\n💭 Mood Distribution:")
    moods = get_mood_distribution(journal)
    for mood_entry in moods:
        mood_name = mood_entry[0]
        count = mood_entry[1]
        percentage = (count / total) * 100
        print(f"   {mood_name}: {count} films ({percentage:.1f}%)")


def check_goals(journal):
    """
    Track watching goals (e.g., 52 films a year)
    """
    display_header("Watching Goals")

    total = len(journal)

    # Goal: 52 films a year (1 per week)
    yearly_goal = 52
    progress = (total / yearly_goal) * 100

    print(f"🎯 Yearly Goal: Watch {yearly_goal} films")
    print(f"📊 Progress: {total}/{yearly_goal} films ({progress:.1f}%)")

    if total >= yearly_goal:
        print("🎉 GOAL ACHIEVED! You're a true cinéphile!")
    else:
        remaining = yearly_goal - total
        print(f"📽️ {remaining} more films to reach your goal!")

    # Bonus: Films per month average
    if total > 0:
        # Simple assumption: journal represents 1 year
        monthly_avg = total / 12
        print(f"\n📅 Average: {monthly_avg:.1f} films per month")

def main():
    """
    Main program loop - coordinates EVERYTHING

    What it does:
        1. Shows welcome message
        2. Displays menu
        3. Gets user choice
        4. Calls appropriate function
        5. Repeats until user exits

    Why: This is the HEART - it makes everything work together!

    Uses: EVERY function we created!
    """
    journal = []  # Our main data structure

    # Welcome message
    print("\n" + "🎬" * 25)
    print("WELCOME TO YOUR CINÉPHILE FILM JOURNAL".center(50))
    print("Track, analyze, and celebrate your love for cinema")
    print("🎬" * 25)

    # Main loop
    while True:
        display_menu()
        choice = get_valid_choice(1, 7)

        if choice == "1":
            add_film(journal)

        elif choice == "2":
            view_all_films(journal)

        elif choice == "3":
            search_films(journal)

        elif choice == "4":
            display_statistics(journal)

        elif choice == "5":
            check_goals(journal)

        elif choice == "6":
            get_random_note(journal)  # type: ignore

        elif choice == "7":
            display_header("Au Revoir!")
            print("Thanks for using your Film Journal!")
            print("Keep watching, keep dreaming! 🎬✨")
            break  # Exit the while loop

        # Wait for user to press Enter before showing menu again
        input("\nPress Enter to continue...")

# Start the program!
if __name__ == "__main__":
    main()
