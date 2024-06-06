# This is the entry point of the application.

from todo_list import ToDoList
from utils import clear_screen, print_menu

def main():
    todo_list = ToDoList()
    
    while True:
        clear_screen()
        print_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            task_name = input("Enter task name: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            priority = input("Enter priority (Low, Medium, High): ").strip()
            category = input("Enter category: ").strip()
            todo_list.add_task(task_name, due_date, priority, category)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: ").strip())
            todo_list.mark_task_completed(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: ").strip())
            todo_list.delete_task(task_id)
        elif choice == '5':
            todo_list.save_tasks()
            print("Tasks saved successfully. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()