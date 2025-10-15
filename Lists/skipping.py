days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperatures = [30, 32, 33, 31, 29]

day_name = "Mon"
if day_name in days:
    index = days.index(day_name)
    new_temp = int(input(f"New temperature for {day_name}: "))
    temperatures[index] = new_temp
    print(f"Updated temperature for {day_name} to {new_temp}")
