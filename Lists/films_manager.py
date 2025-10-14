print("🎬 Welcome to Favorite Films Manager!")

# Step 1: Start with a list of films
favorite_films = ["City of God", "In the Mood for Love", "Incendies", "Come and See", "Paris Texas"]

# Step 2: Start the loop
while True:
    print("\n--- Menu ---")
    print("1. See your films")
    print("2. Add a film")
    print("3. Remove a film")
    print("4. Count films")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print("\nYour favorite films:")
        for film in favorite_films:
            print(f"- {film}")

    elif choice == "2":
        new_film = input("Enter the film you want to add: ")
        favorite_films.append(new_film)
        print(f"{new_film} has been added!")

    elif choice == "3":
        remove_film = input("Enter the film you want to remove: ")
        if remove_film in favorite_films:
            favorite_films.remove(remove_film)
            print(f"{remove_film} has been removed!")
        else:
            print(f"{remove_film} is not in your list!")

    elif choice == "4":
        print(f"You have {len(favorite_films)} films in your list.")

    elif choice == "5":
        print("Thanks for using Favorite Films Manager! Goodbye 🎬")
        break

    else:
        print("Invalid option. Please choose 1-5.")
