points = 0

for i in range(1, 6):        # i = 1,2,3,4,5
    if i % 2 == 0:           # if i is divisible by 2 → even
        points += 2          # add 2 points for even
    else:                     # otherwise → odd
        points += 1          # add 1 point for odd
    print(f"Round {i}, points: {points}")
