# 1. Welcome the user
print("Welcome to your To-Do List, let's get shit done!")

# 2. Create an empty list to store tasks
tasks = []

# 3. Start infinite loop so user can keep managing tasks
while True:
    # 4. Show options to the user
    print("\nOptions:")
    print("1. Add task")
    print("2. Remove task")
    print("3. List tasks")
    print("4. Quit")

    # 5. Get user choice
    choice = input("Choose an option (1-4): ")

    # 6. Add a task
    if choice == '1':
        task = input("Enter the task you lazy bastard: ")
        tasks.append(task)
        print(f"Task added: {task}")

    # 7. Remove a task
    elif choice == '2':
        if not tasks:
            print("No tasks to remove, you slacker!")
            continue
        # Show tasks with numbers
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid number, idiot!")

    # 8. List all tasks
    elif choice == '3':
        if not tasks:
            print("No tasks, you’re chilling too much!")
        else:
            print("Your tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    # 9. Quit
    elif choice == '4':
        print("Exiting To-Do List. Go conquer the world, champ!")
        break

    # 10. Invalid input
    else:
        print("Invalid choice, try again you fool!")
