# This file contains the 'ToDoList' class to manage the list of tasks.

import json
from task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, name, due_date, priority, category):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, name, due_date, priority, category)
        self.tasks.append(new_task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task {task_id} not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} deleted.")
                return
        print(f"Task {task_id} not found.")

    def save_tasks(self):                                    # Function to write tasks to the JSON file
        tasks_data = [task.__dict__ for task in self.tasks]
        with open('data_tasks.json', 'w') as file:
            json.dump(tasks_data, file, indent=4)

    def load_tasks(self):                                    # Function to read tasks from the JSON file
        try:
            with open('data_tasks.json', 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**data) for data in tasks_data]
        except FileNotFoundError:
            self.tasks = []