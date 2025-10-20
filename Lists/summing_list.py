numbers = [10, 20, 30, 40]
total = sum(numbers)
print(total)

numbers = [100, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print(total)

numbers = [10, 20, 30, 40, 50, 60]
total = sum(num for num in numbers if num > 20)
print(total)

numbers = [5, 15, 25, 35, 45]
total = sum(filter(lambda x: x > 20, numbers))
print(total)

matrix = [[1, 2], [3, 4], [5, 6]]

total = sum(sum(inner) for inner in matrix)
print(total)

items = [10, "20", 30]       # Mixed integers and string numbers
total = sum(int(x) for x in items)
print(total)
