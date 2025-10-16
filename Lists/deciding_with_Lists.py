days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [4500, 8000, 3000, 6000, 4000, 9500, 7000]

for i in range(len(steps)): #range(7) also works but less flexible
    if steps[i] < 5000:
        steps[i] *= 2
        print(f"On {days[i]}, you walked less than 5000 steps. Steps doubled to {steps[i]}.")

    elif steps[i] <= 8000:
        print(f"On {days[i]}, you walked a moderate amount of {steps[i]} steps.")

    else:
        print(f"On {days[i]}, you walked a lot with {steps[i]} steps!")
