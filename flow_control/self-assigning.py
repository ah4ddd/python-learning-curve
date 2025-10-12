# Start the log
daily_log = "Today's log:"

# Morning
morning_activity = " Woke up and had breakfast."
daily_log = daily_log + morning_activity  # self-assign

# Work / Study
work_activity = " Worked on Python projects."
daily_log = daily_log + work_activity  # add more

# Exercise
exercise_activity = " Did a workout session."
daily_log = daily_log + exercise_activity

# Evening
evening_activity = " Watched a movie and relaxed."
daily_log = daily_log + evening_activity

# Night
night_activity = " Went to bed at 11 PM."
daily_log += night_activity  # using += this time

# Print final log
print(daily_log)

# Optional: Track how many tasks you did
tasks_completed = 0
tasks_completed += 1  # Morning
tasks_completed += 1  # Work
tasks_completed += 1  # Exercise
tasks_completed += 1  # Evening
tasks_completed += 1  # Night

print(f"\nTotal tasks completed today: {tasks_completed}")
