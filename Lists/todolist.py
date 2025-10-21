from collections import Counter

print("🧠 The Ruthless To-Do Commander")
print("------------------------------")

tasks = []

while True:
    print("\nWhat do you want to do?")
    print("1️⃣ Add Task")
    print("2️⃣ View All Tasks")
    print("3️⃣ Mark Task as Completed")
    print("4️⃣ Delete Task")
    print("5️⃣ Show Stats")
    print("6️⃣ Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Task name: ")
        priority = int(input("Priority (1 = low, 5 = high): "))
        hours = float(input("Estimated hours: "))
        completed = False
        tasks.append([name, priority, hours, completed])
        print(f"✅ Task '{name}' added successfully!")

    elif choice == "2":
        if not tasks:
            print("⚠️ No tasks yet.")
        else:
            print("\n📝 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✅ Done" if task[3] else "⏳ Pending"
                print(f"{i}. {task[0]} | Priority: {task[1]} | Hours: {task[2]} | {status}")

    elif choice == "3":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task[0]}")
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index][3] = True
            print(f"✅ '{tasks[index][0]}' marked as completed!")
        else:
            print("❌ Invalid task number.")

    elif choice == "4":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task[0]}")
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"🗑️ '{deleted[0]}' deleted successfully!")
        else:
            print("❌ Invalid task number.")

    elif choice == "5":
        if not tasks:
            print("⚠️ No data to show stats for.")
            continue

        total_tasks = len(tasks)
        completed_tasks = sum(1 for t in tasks if t[3])
        pending_tasks = total_tasks - completed_tasks
        total_hours = sum(t[2] for t in tasks)

        # Count priority levels using Counter
        priority_levels = Counter(t[1] for t in tasks)

        print("\n📊 Task Stats:")
        print(f"Total tasks: {total_tasks}")
        print(f"Completed: {completed_tasks} | Pending: {pending_tasks}")
        print(f"Total estimated hours: {total_hours}")
        print("Priority Breakdown:")
        for level, count in sorted(priority_levels.items()):
            print(f"  Priority {level}: {count} tasks")

        # Sort tasks by priority for overview
        sorted_tasks = sorted(tasks, key=lambda x: x[1], reverse=True)
        summary = " | ".join(t[0] for t in sorted_tasks)
        print(f"\n🗒️ Priority Summary: {summary}")

    elif choice == "6":
        print("\n👋 Exiting The Ruthless To-Do Commander...")
        break

    else:
        print("❌ Invalid choice, try again.")
