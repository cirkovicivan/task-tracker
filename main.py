import sys
import json
from pathlib import Path

file = Path("data.json")


def add_task(task_name):
    if file.is_file():
        with open(file, "r") as f:
            data = json.load(f)
    else:
        data = []

    next_id = max([task["id"] for task in data], default=0) + 1

    content = {
        "id": next_id,
        "name": task_name,
        "status": "in progress"
    }

    data.append(content)

    with open("data.json", "w") as f:
        json.dump(content, f, indent=4)


def delete_task(task_id):
    task_id = int(task_id)

    with open("data.json", "r") as f:
        data = json.load(f)

    data = [task for task in data if task["id"] != task_id]

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    _, function, task_data = sys.argv

    match function:
        case "add":
            add_task(task_data)
        case "delete":
            delete_task(task_data)
