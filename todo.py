#!/usr/bin/env python3
def main():
    tasks = [
        {"task": "Buy groceries", "done": False},
        {"task": "Read a book", "done": False},
        {"task": "Write code", "done": False},
        {"task": "Go for a run", "done": False},
        {"task": "Call a friend", "done": False},
        {"task": "Clean the house", "done": False},
        {"task": "Pay bills", "done": False},
        {"task": "Prepare dinner", "done": False},
        {"task": "Water the plants", "done": False},
        {"task": "Check emails", "done": False}
    ]

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Edit Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add: "))
            
            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            if tasks:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")
            else:
                print("No tasks found.")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            task_index = int(input("Enter the task number you want to edit: ")) - 1
            if 0 <= task_index < len(tasks):
                task = input("Enter the new task description: ")
                tasks[task_index]["task"] = task
                print("Task is edited!")  
            else:
                print("Invalid task number.")

        elif choice == '5':
            task_index = int(input("Enter the task number you want to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                print("Task deleted!")      
            else:
                print("Invalid task number.")

        elif choice == '6':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()