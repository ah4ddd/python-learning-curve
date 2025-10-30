def analyze_scores(scores):
    total = sum(scores)
    average = total / len(scores)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    else:
        grade = "C"

    return (total, average, grade)

total, avg, grade = analyze_scores([90, 80, 70, 100])
print(f"Total: {total}, Average: {avg}, Grade: {grade}")
