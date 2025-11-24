# module3_storage.py
import json

def save_data(user):
    data = {
        "name": user.get_name(),
        "tasks": [
            {"title": t.title, "subject": t.subject, "hours": t.hours, "completed": t.completed}
            for t in user.tasks
        ]
    }
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
