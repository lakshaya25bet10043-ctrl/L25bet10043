# module2_tasks.py
class Task:
    def __init__(self, title, subject, hours):
        self.title = title
        self.subject = subject
        self.hours = hours
        self.completed = False

    def mark_complete(self):
        self.completed = True
