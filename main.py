import json
import os
from datetime import datetime
from InquirerPy import inquirer

TASKS_DIR = os.path.expanduser("~/.taskmanager")
TASKS_FILE = os.path.join(TASKS_DIR, "tasks.json")

def ensure_directory_exists():
    if not os.path.exists(TASKS_DIR):
        os.makedirs(TASKS_DIR)

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    ensure_directory_exists()
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def format_task(task):
    status = "[X]" if task.get("done") else "[ ]"
    due_date = f" (Due: {task['due_date']})" if task.get("due_date") else ""
    repeat = f" (Repeats: {task['repeat']})" if task.get("repeat") else ""
    return f"{status} {task['name']}{due_date}{repeat}"

def main():
    tasks = load_tasks()

    while True:
        choice = inquirer.select(
            message="Choose an action",
            choices=[
                "List tasks",
                "Add a task",
                "Remove a task",
                "Quit"
            ]
        ).execute()

        if choice == "List tasks":
            if not tasks:
                print("No tasks available.")
            else:
                for idx, task in enumerate(tasks):
                    print(f"{idx}. {format_task(task)}")

        elif choice == "Add a task":
            task_name = inquirer.text(message="Enter new task").execute()
            due_date = inquirer.text(message="Enter due date (YYYY-MM-DD, optional)").execute()
            repeat = inquirer.select(
                message="Set task repetition",
                choices=["None", "Daily", "Weekly", "Monthly"],
                default="None"
            ).execute()
            if task_name:
                task = {
                    "name": task_name,
                    "done": False,
                    "due_date": due_date if due_date else None,
                    "repeat": repeat if repeat != "None" else None
                }
                tasks.append(task)
                save_tasks(tasks)
                print("Task added.")

        elif choice == "Remove a task":
            if not tasks:
                print("No tasks to remove.")
                continue
            task_num = inquirer.select(
                message="Select a task to remove",
                choices=[f"{idx}. {task['name']}" for idx, task in enumerate(tasks)]
            ).execute()
            task_index = int(task_num.split('.')[0])
            if 0 <= task_index < len(tasks):
                del tasks[task_index]
                save_tasks(tasks)
                print("Task removed.")

        elif choice == "Quit":
            break

if __name__ == "__main__":
    main()
