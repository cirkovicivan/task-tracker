import sys
import json
from pathlib import Path
from datetime import datetime

file = Path(__file__).parent / "data.json"


def add_task(task_name):
    if file.is_file():
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = []

    next_id = max([task["id"] for task in data], default=0) + 1

    content = {
        "id": next_id,
        "description": task_name,
        "status": "todo",
        "created_at": datetime.now().isoformat(),
        "updated_at": ""
    }

    data.append(content)

    with open(file, "w") as f:
        json.dump(data, f, indent=4)


def delete_task(task_id):
    task_id = int(task_id)

    with open("data.json", "r") as f:
        data = json.load(f)

    data = [task for task in data if task["id"] != task_id]

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def update_task(task_id, task_content):
    if not task_id or not task_content:
        raise Exception("Not valid format of command please type --help")

    with open(file, "r") as f:
        data = json.load(f)

    for task in data:
        if task["id"] == int(task_id):
            task["description"] = task_content
            task["updated_at"] = datetime.now().isoformat()

    with open(file, "w") as f:
        json.dump(data, f, indent=4)


def list_tasks(type):
    with open(file, "r") as f:
        tasks = json.load(f)

    match type:
        case "done":
            filtered_tasks = [task for task in tasks if task["status"] == "done"]
        case "todo":
            filtered_tasks = [task for task in tasks if task["status"] == "todo"]
        case "in-progress":
            filtered_tasks = [task for task in tasks if task["status"] == "in progress"]
        case _:
            filtered_tasks = tasks

    if not filtered_tasks:
        print("There is no tasks with that status")
    else:
        print(filtered_tasks)


def mark_done(task_id):
    with open(file, "r") as f:
        data = json.load(f)

    for task in data:
        if task["id"] == int(task_id):
            task["status"] = "done"

    with open(file, "w") as f:
        json.dump(data, f, indent=4)


def mark_in_progress(task_id):
    with open(file, "r") as f:
        data = json.load(f)

    for task in data:
        if task["id"] == int(task_id):
            task["status"] = "in progress"

    with open(file, "w") as f:
        json.dump(data, f, indent=4)


def main():
    function = sys.argv[1] if len(sys.argv) > 1 else ""
    task_data = sys.argv[2] if len(sys.argv) > 2 else ""
    task_data1 = sys.argv[3] if len(sys.argv) > 3 else ""

    match function:
        case "add":
            add_task(task_data)
        case "delete":
            delete_task(task_data)
        case "list":
            list_tasks(task_data)
        case "update":
            update_task(task_data, task_data1)
        case "mark-done":
            mark_done(task_data)
        case "mark-in-progress":
            mark_in_progress(task_data)
        case _:
            print("That command does not exist, type help for more info.")


if __name__ == '__main__':
    main()
