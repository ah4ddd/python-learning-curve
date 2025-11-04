numbers = [1, 2, 3, 2, 4, 2]

print(numbers.count(2))  # 3 (appears 3 times)
print(numbers.count(1))  # 1 (appears once)


alex_friends = ["morgan", "jordan", "casey", "taylor", "riley"]
jordan_friends = ["casey", "taylor", "avery", "cameron", "morgan"]

# Who are their mutual friends?
mutual_friends = set(alex_friends) & set(jordan_friends)

print(f"Mutual friends: {mutual_friends}")
# ['morgan', 'casey', 'taylor']
