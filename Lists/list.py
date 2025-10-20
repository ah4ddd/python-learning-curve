astronauts = ["Neil", "Buzz", "Yuri", "Valentina"]
scores = [85, 92, 78, 95]

sorted_scores = sorted(scores)
print("Original scores:", scores)
print("Sorted copy of scores:", sorted_scores)

scores.sort()
print("Original scores after sort():", scores)

combined = list(zip(astronauts, scores))
print("Astronauts paired with sorted scores:", combined)

combined.sort(key=lambda x: x[1])
print("Combined sorted by score:", combined)
