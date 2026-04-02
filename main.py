import sys
import json
from pathlib import Path

file = Path("data.json")

def add_task(task):
    content = {
        "name": task,
        "status": "in progress"
    }

    if file.is_file():
        with open("data.json", "rb+") as f:
            size = f.tell()
            f.seek(size-1, 2)
            f.truncate()  # delete the last char
            f.write((", " + json.dumps(content) + "]").encode("utf-8"))
    else:
        with open("data.json", "w") as f:
            f.write("[" + json.dumps(content) + "]")

if __name__ == '__main__':
    user_input = input("Please enter your task: ")
    add_task(user_input)

