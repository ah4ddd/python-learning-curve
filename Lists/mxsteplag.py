days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [5000, 8000, 7000, 6000, 9000, 7500, 6500]

print (max(steps))

sorted_steps = sorted(steps, reverse=True)
print("Steps from highest to lowest:", sorted_steps)

max_steps_day = days[steps.index(max(steps))]
print(f"Hottest step day: {max_steps_day} with {max(steps)} steps")


# max(steps) → finds the biggest number, e.g. 9000.

# steps.index(max(steps)) → finds the position of that number in the list → 4.

# days[4] → uses that position to grab the day name from the days list → "Fri".

# So max_steps_day = days[steps.index(max(steps))]

# → means “give me the day that matches the highest step count.”
