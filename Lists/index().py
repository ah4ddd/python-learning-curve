days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
temp = [30, 32, 33, 31, 29, 27, 26]

print(days)
print("\n", temp)

day_name = input("Enter day name: ").lower()
if day_name in days:
    index = days.index(day_name)
    update_temp = int(input(f"Enter temperature for {day_name}: "))
    temp[index] = update_temp

    print(f"Updated temperature for {day_name} to {update_temp}")

    average_temp = sum(temp) / len(temp)
    hottest_day = days[temp.index(max(temp))]
    coldest_day = days[temp.index(min(temp))]

    print(f"Average temperature: {average_temp}")
    print(f"Hottest day: {hottest_day} with {max(temp)}°C")
    print(f"Coldest day: {coldest_day} with {min(temp)}°C")
else:
    print("Invalid day name.")
