numbers = [45, 89, 12, 36, 74]

max_num = numbers[0]
min_num = numbers[0]

for n in numbers:
    if n > max_num:
        max_num = n
    if n < min_num:
        min_num = n

print("Max:", max_num)
print("Min:", min_num)
