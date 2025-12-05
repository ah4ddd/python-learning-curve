class Habit:
    def __init__(self, name, streak=0):
        self.name = name
        self.streak = streak

    def __str__(self):
        return f"{self.name} 🔥 Streak: {self.streak}"

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}(name={self.name!r}, streak={self.streak})"

    def __add__(self, days):
        new_habit = Habit(self.name, self.streak + days)
        return new_habit

    def __call__(self):
        self.streak += 1
        return f"Completed: {self.name}"

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

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}(habits={self.habits!r})"

    def __str__(self):
        if not self.habits:
            return "HabitTracker (no habits yet)"
        names = ", ".join(h.name for h in self.habits)
        return f"HabitTracker tracking: {names}"

ht = HabitTracker()

gym = Habit("Gym")
coding = Habit("Coding")
reading = Habit("Reading")

ht.add(gym)
ht.add(coding)
ht.add(reading)

gym()
coding()
gym = gym + 2

print(ht)
print(repr(ht))
print([gym, coding, reading])

