# Unit tests for the 'ToDoList' class.

import unittest
from todo_list import ToDoList
from task import Task

class TestToDoManager(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        self.todo_list.add_task("Test Task", "2024-12-31", "High", "Work")
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0].name, "Test Task")

    def test_mark_task_completed(self):
        self.todo_list.add_task("Test Task", "2024-12-31", "High", "Work")
        self.todo_list.mark_task_completed(1)
        self.assertTrue(self.todo_list.tasks[0].completed)

    def test_delete_task(self):
        self.todo_list.add_task("Test Task", "2024-12-31", "High", "Work")
        self.todo_list.delete_task(1)
        self.assertEqual(len(self.todo_list.tasks), 0)

if __name__ == "__main__":
    unittest.main()