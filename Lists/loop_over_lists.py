days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [4500, 8000, 3000, 6000, 4000, 7500, 6500]

for i in range(len(steps)):
    if steps[i] < 5000:
        steps[i] = steps[i] * 2  # Double low step days

for index, step in enumerate(steps):
    print(f"{days[index]}: {step} steps")
