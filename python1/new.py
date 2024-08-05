import os

# Define the filename for storing tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task.startswith("[x]") else "[ ]"
            print(f"{i}. {status} {task[4:]}")

def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(f"[ ] {task}")
        save_tasks(tasks)
        print("Task added.")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            tasks[task_number - 1] = "[x] " + task[4:]
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the To-Do List application."""
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
