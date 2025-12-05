class Habit:
    def __init__(self, name):
        self.name = name
        self.streak = 0

    def __str__(self):
        return f"{self.name} - Streak: {self.streak}"

    def __repr__(self):
        return f"Habit('{self.name}', streak={self.streak})"

    def __add__(self, days):
        new_habit = Habit(self.name)
        new_habit.streak = self.streak + days
        return new_habit

    def __call__(self):
        self.streak += 1
        return f"Nice! You completed {self.name} today."

class HabitTracker:
    def __init__(self):
        self.habits = []

    def add(self, habit):
        self.habits.append(habit)

    def __len__(self):
        return len(self.habits)

    def __getitem__(self, index):
        return self.habits[index]

    def __iter__(self):
        return iter(self.habits)

    def __str__(self):
        return f"HabitTracker with {len(self)} habits."

ht = HabitTracker()

gym = Habit("Gym")
coding = Habit("Coding")
reading = Habit("Reading")

ht.add(gym)
ht.add(coding)
ht.add(reading)

print(f"{ht}\n")

print(gym())
print(coding())
print(reading())

print()
gym = gym + 2
print(repr(gym))
print([gym])

print("\nCurrent Habits:")
for h in ht:
    print(h)

print("\nSecond habit:", ht[1])



