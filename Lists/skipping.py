# Weekdays
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Daily temperatures (°C)
temperatures = [22, 24, 19, 23, 25, 21, 20]

print("🔥 Welcome to the Full Temperature Tracker 🔥")

print("\nWeekly temperatures:")
for day, temp in zip(days, temperatures):
    print(f"{day}: {temp}°C")

# Slice Tue to Fri (indexes 1 to 5 → skips 5)
midweek_days = days[1:5]
midweek_temps = temperatures[1:5]

print("\n📌 Midweek temperatures (Tue-Fri):")
for day, temp in zip(midweek_days, midweek_temps):
    print(f"{day}: {temp}°C")

average_midweek = sum(midweek_temps) / len(midweek_temps)
hottest = max(midweek_temps)
coldest = min(midweek_temps)

hottest_day = midweek_days[midweek_temps.index(hottest)]
coldest_day = midweek_days[midweek_temps.index(coldest)]

print(f"\nAverage midweek temperature: {average_midweek:.1f}°C")
print(f"Hottest midweek day: {hottest_day} ({hottest}°C)")
print(f"Coldest midweek day: {coldest_day} ({coldest}°C)")

while True:
    print("\nOptions: ")
    print("1 - Update a temperature")
    print("2 - Add a new day")
    print("3 - View midweek slice")
    print("4 - Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        day_name = input("Enter day to update (Mon-Sun): ")
        if day_name in days:
            index = days.index(day_name)
            new_temp = int(input(f"New temperature for {day_name}: "))
            temperatures[index] = new_temp
            print(f"{day_name} updated to {new_temp}°C")
        else:
            print("Invalid day!")

    elif choice == "2":
        new_day = input("Enter new day name: ")
        new_temp = int(input(f"Temperature for {new_day}: "))
        days.append(new_day)
        temperatures.append(new_temp)
        print(f"{new_day} added with {new_temp}°C")

    elif choice == "3":
        start = int(input("Start index (Python-style, 0 = Mon): "))
        end = int(input("End index (Python-style, last index not included): "))
        slice_days = days[start:end]
        slice_temps = temperatures[start:end]
        print("\n📌 Sliced temperatures:")
        for d, t in zip(slice_days, slice_temps):
            print(f"{d}: {t}°C")
        print(f"Slice length: {len(slice_temps)}")

    elif choice == "4":
        print("\nThanks for using Temperature Tracker! ❄️🔥")
        break

    else:
        print("Invalid option! Try again.")

    # Show all temperatures after every action
    print("\nCurrent weekly temperatures:")
    for day, temp in zip(days, temperatures):
        print(f"{day}: {temp}°C")

