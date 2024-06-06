# Utility functions to clear the screen and print the menu.

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print("To-Do List Manager")
    print("==================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save and Exit")