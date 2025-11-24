# module5_reminders.py
def generate_reminder(task):
    if not task.completed:
        return f"Reminder: Complete '{task.title}' for {task.subject}!"
    return f"'{task.title}' already completed."

