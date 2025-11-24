# module4_analyzer.py
def calculate_productivity(tasks):
    if not tasks:
        return 0
    completed = len([t for t in tasks if t.completed])
    return (completed / len(tasks)) * 100
