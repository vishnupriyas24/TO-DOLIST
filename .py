class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False
class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.name} - Due: {task.due_date} - Completed: {task.completed}")
todo_list = ToDoList()
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")
        task = Task(name, description, due_date)
        todo_list.add_task(task)
        print("Task added successfully!")
    elif choice == '2':
        print("\n--- Tasks ---")
        todo_list.view_tasks()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
