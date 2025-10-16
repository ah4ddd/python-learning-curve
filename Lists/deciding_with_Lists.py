temps = [22, 28, 31, 19, 25]
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
steps = [4500, 8000, 3000, 6000, 7000]

for temp in temps:
    if temp > 30:
        print(f"{temp}°C → Too hot!")
    elif temp < 20:
        print(f"{temp}°C → Too cold!")
    else:
        print(f"{temp}°C → Just right.")

for i in range(len(temps)):
    if temps[i] > 30:
        print(f"{days[i]} → Too hot!")

for index,days in enumerate(days):
    print(f"{days} had {steps[index]} steps")


for i in range(len(steps)):
    if steps[i] < 5000:
        steps[i] *= 2

print(steps)
