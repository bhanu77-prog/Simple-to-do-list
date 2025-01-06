
# Simple To-Do List

# Initialize an empty list to store tasks
tasks = []

# Function to display the menu
def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

# Function to add a task
def add_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks added yet.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{i}. {task['task']} - {status}")

# Function to mark a task as complete
def complete_task():
    if not tasks:
        print("No tasks to complete.")
        return
    view_tasks()
    task_num = int(input("Enter the task number to mark as complete: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

# Main program loop
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
