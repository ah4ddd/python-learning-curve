from name_function import get_formatted_name

print("Enter q to exit")

while True:
    first = input("\nPlease give me a first name: ")
    if first == "q":
        break
    last = input("\nEnter your last name: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly Formatted name: {formatted_name}")
