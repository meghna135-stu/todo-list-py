import json

# Load tasks
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

# Save tasks
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark as complete")
    print("5. Clear All Tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        save_tasks()
        print("Task added!")

    # View Tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else "✗"
                print(f"{i}. {task['task']} [{status}]")

    # Delete Task
    elif choice == "3":
        if not tasks:
            print("No tasks to delete")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")

            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    save_tasks()
                    print("Task deleted!")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number")

    # Mark Complete
    elif choice == "4":
        if not tasks:
            print("No tasks available")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['task']}")

            try:
                num = int(input("Enter task number to mark complete: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["done"] = True
                    save_tasks()
                    print("Task marked as complete!")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number")

    # Clear All
    elif choice == "5":
        confirm = input("Are you sure? (y/n): ")
        if confirm.lower() == "y":
            tasks.clear()
            save_tasks()
            print("All tasks cleared!")

    # Exit
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")