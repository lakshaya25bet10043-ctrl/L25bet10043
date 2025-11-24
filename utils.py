# module7_utils.py
def print_line():
    print("-" * 40)

def input_task():
    title = input("Enter task title: ")
    subject = input("Enter subject: ")
    hours = int(input("Enter hours required: "))
    return title, subject, hours
