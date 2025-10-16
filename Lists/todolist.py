task = []

print("\nWelcome to your To-Do List Manager!\n")
print("\n1. View To-Do List")
print("2. Add Task")
print("3. Mark task as done")
print("4. Remove Task")
print("5. Exit\n")



choice = input("choose an option: ")

if choice == "2":
    task_name = input("Enter the task name: ")
    task.append(task_name)
    print(f'Task "{task_name}" added to the list.')

elif choice == "1":
    if not task:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for idx, t in enumerate(task, start=1):
            print(f"{idx}. {t}")

elif choice == "3":
    if not task:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for idx, t in enumerate(task, start=1):
            print(f"{idx}. {t}")
        done_idx = int(input("Enter the number of the task you completed: ")) - 1
        if 0 <= done_idx < len(task):
            completed_task = task.pop(done_idx)
            print(f'Task "{completed_task}" marked as done and removed from the list.')
        else:
            print("Invalid task number.")

elif choice == "4":
    if not task:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for idx, t in enumerate(task, start=1):
            print(f"{idx}. {t}")
        remove_idx = int(input("Enter the number of the task you want to remove: ")) - 1
        if 0 <= remove_idx < len(task):
            removed_task = task.pop(remove_idx)
            print(f'Task "{removed_task}" removed from the list.')
        else:
            print("Invalid task number.")

elif choice == "5":
    print("Exiting the To-Do List Manager. Goodbye!")
else:
    print("Invalid choice. Please select a valid option.")

