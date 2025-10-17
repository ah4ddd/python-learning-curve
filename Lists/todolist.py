tasks = []  # list to store tasks

while True:  # infinite loop keeps the program running
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Quit")

    choice = input("Choose an option: ")

    # VIEW TASKS
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):        # loop through list indexes
                print(f"{i+1}. {tasks[i]}")    # i+1 so it starts counting from 1

    # ADD TASK
    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print(f"Task '{new_task}' added!")

    # MARK TASK AS DONE
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            task_num = int(input("Enter task number to mark done: "))
            if 0 < task_num <= len(tasks):
                tasks[task_num - 1] += " ✅"
                print(f"Task {task_num} marked as done!")
            else:
                print("Invalid task number.")

    # DELETE TASK
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            task_num = int(input("Enter task number to delete: "))
            if 0 < task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed '{removed}'")
            else:
                print("Invalid task number.")

    # QUIT PROGRAM
    elif choice == "5":
        print("Goodbye!")
        break

    # WRONG CHOICE HANDLER
    else:
        print("Invalid option. Please try again.")
