colors = {"red", "blue", "green"}

print(colors)

colors.add( "liquid")

print(colors)

colors = {"red", "blue"}

print(colors)

colors.update(["green", "yellow", "purple", "red"])

print(colors)

numbers = {1, 2, 3}

numbers.update([4, 5, 6])
print(numbers)

numbers.update((7, 8))
print(numbers)

numbers.update({9, 10})
print(numbers)

user1_tags = {"python", "coding", "music"}
user2_tags = {"music", "art", "gaming"}

user1_tags.update(user2_tags)

print(user1_tags)

colors = {"red", "blue", "green", "yellow"}

colors.remove("blue")

print(colors)

colors = {"red", "blue", "green", "yellow"}

colors.discard("blue")

print(colors)

colors = {"red", "blue", "green", "yellow"}

removed = colors.pop()

print(f"Removed: {removed}")
print(colors)

colors = {"red", "blue", "green", "yellow"}

for color in colors:
    print(color)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1 | set2 | colors

print(result)

result = set1.union(set2)

print(result)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1 & set2

print(result)

result = set1 - set2

print(result)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 - set2)
print(set2 - set1)

result = set1 ^ set2

print(result)

print(set1 == set2)

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1 <= set2)
print(set1 >= set2)

print(set1.isdisjoint(set2))

result = set1.intersection(set2)

print(result)

set_A = {1, 2, 3}
set_B = {1, 2, 3, 4, 5}

print(set_A.issubset(set_B))

set_C = {1, 6}
print(set_C.issubset(set_B))

set_A = {1, 2, 3}
set_B = {1, 2, 3, 4, 5}

print(set_B.issuperset(set_A))

set_D = {1, 2}
print(set_A.issuperset(set_D))
