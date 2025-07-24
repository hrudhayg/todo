# todo.py

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added!")
    else:
        print("Task cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    try:
        view_tasks(tasks)
        choice = int(input("Enter the number of the task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        show_menu()
        try:
            choice = input("Select an option (1-4): ").strip()
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                delete_task(tasks)
            elif choice == "4":
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid selection. Choose between 1–4.")
        except Exception as e:
            print("An unexpected error occurred:", str(e))
        finally:
            print("-" * 30)

if __name__ == "__main__":
    main()
