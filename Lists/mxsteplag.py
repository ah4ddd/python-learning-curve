days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [5000, 8000, 7000, 6000, 9000, 7500, 6500]

print (max(steps))

sorted_steps = sorted(steps, reverse=True)
print("Steps from highest to lowest:", sorted_steps)

max_steps_day = days[steps.index(max(steps))]
print(f"Hottest step day: {max_steps_day} with {max(steps)} steps")
