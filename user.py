# module1_user.py
class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def get_name(self):
        return self.name

    def add_task(self, task):
        self.tasks.append(task)
