# This file contains the 'Task' class to represent individual tasks.

class Task:
    def __init__(self, task_id, name, due_date, priority, category, completed=False):
        self.task_id = task_id
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.task_id}: {self.name} | Due: {self.due_date} | Priority: {self.priority} | Category: {self.category} | Status: {status}"