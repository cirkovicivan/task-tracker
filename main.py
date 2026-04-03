import sys
import json
from pathlib import Path
from datetime import datetime

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
        "description": task_name,
        "status": "in progress",
        "created_at": datetime.now().isoformat(),
        "updated_at": ""
    }

    data.append(content)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def delete_task(task_id):
    task_id = int(task_id)

    with open("data.json", "r") as f:
        data = json.load(f)

    data = [task for task in data if task["id"] != task_id]

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def list():
    with open(file, "r") as f:
        data = json.load(f)
    print(data)


if __name__ == '__main__':

    function = sys.argv[1] if len(sys.argv) > 1 else ""
    task_data = sys.argv[2] if len(sys.argv) > 2 else ""

    match function:
        case "add":
            add_task(task_data)
        case "delete":
            delete_task(task_data)
        case "list":
            list()
