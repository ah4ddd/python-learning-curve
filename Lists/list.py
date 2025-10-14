# Temperature Tracker
temperatures = [20, 22, 25, 23, 24]

print("🌡️ Current Temperatures:", temperatures)

# Update a reading (single)
temperatures[2] = 26
print("Updated 3rd reading:", temperatures)

# Update multiple readings (slice)
temperatures[1:4] = [21, 27, 28]
print("Updated 2nd to 4th readings:", temperatures)

# Add new readings
temperatures.append(29)
temperatures.append(30)
print("After adding new readings:", temperatures)

# Remove a wrong reading
wrong = temperatures.pop(3)  # removes 4th
print(f"Removed wrong reading: {wrong}")
print("Temperatures now:", temperatures)

# Dynamically increase all readings by 1 (like warming up)
for i in range(len(temperatures)):
    temperatures[i] += 1
print("After increasing all readings by 1:", temperatures)

# Show average temperature
average = sum(temperatures) / len(temperatures)
print(f"Average Temperature: {average:.2f}°C")

# list[start:end] → starts at 'start' index, goes **up to but NOT including** 'end' index
