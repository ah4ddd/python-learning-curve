student_names = ["Alex", "Ben", "Cara", "Dev", "Eva", "Fara"]
scores = [78, 42, 90, 55, 33, 61]

def analyze_scores(names_list, score_list):
    passing_students = []

    for name, score in zip(names_list, score_list):
        print(f"Student: {name:<10} Scored: {score}")

        if score >= 50:
            print("  ✅ Passed")
            passing_students.append(name)
        else:
            print("  ❌ Failed")

    return passing_students

passed = analyze_scores(student_names, scores)

print("\n--- Summary ---")
print(f"Students who passed: {passed}")

