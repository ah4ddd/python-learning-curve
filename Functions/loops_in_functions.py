habits = ["Exercise", "Read", "Meditate", "Study Python"]
days = 7

def track_habit(habit, days):
    completion = []
    for day in range(1, days+1):
        done = input(f"Did you do {habit} on day {day}? (y/n): ").lower()
        if done == "y":
            completion.append(1)
        else:
            completion.append(0)
    return completion

all_habits_completion = []

for habit in habits:
    result = track_habit(habit, days)
    all_habits_completion.append(result)

def analyze_habits(habits, completion_lists):
    for i, habit in enumerate(habits):
        total_done = sum(completion_lists[i])
        percentage = (total_done / len(completion_lists[i])) * 100
        print(f"{habit}: Done {total_done}/{len(completion_lists[i])} days ({percentage:.2f}%)")

print("\n--- Weekly Habit Summary ---")
analyze_habits(habits, all_habits_completion)
