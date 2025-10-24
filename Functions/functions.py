def generate_report(student_name, math_score, science_score, english_score):
    total = math_score + science_score + english_score
    average = total / 3

    print(f"📊 Report Card for {student_name}")
    print("=" * 40)
    print(f"Math: {math_score}")
    print(f"Science: {science_score}")
    print(f"English: {english_score}")
    print("-" * 40)
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    else:
        grade = "C"

    print(f"Grade: {grade}")
    print("=" * 40)
    return average

alice_avg = generate_report("Alice", 95, 88, 92)
bob_avg = generate_report("Bob", 78, 82, 85)
charlie_avg = generate_report("Charlie", 65, 70, 68)
