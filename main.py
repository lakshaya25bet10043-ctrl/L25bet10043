#from user import User
from takes import Task
from storage import save_data, load_data
from analyzer import calculate_productivity
from reminders import generate_reminder
from report import generate_report
from utils import print_line, input_task

def main():
    print("Welcome to Smart Study Planner")
    data = load_data()

    if data:
        user = User(data["name"])
        for t in data["tasks"]:
            task = Task(t["title"], t["subject"], t["hours"])
            if t["completed"]:
                task.mark_complete()
            user.add_task(task)
        print("Loaded existing data.")
    else:
        name = input("Enter your name: ")
        user = User(name)

    print_line()
    print("1. Add Task")
    print("2. Mark Task Complete")
    print("3. Show Report")
    print("4. Save & Exit")
    print_line()

    while True:
        choice = input("Choose option: ")

        if choice == "1":
            title, subject, hours = input_task()
            user.add_task(Task(title, subject, hours))
            print("Task added.")

        elif choice == "2":
            for i, t in enumerate(user.tasks):
                print(i, t.title)
            idx = int(input("Enter task number: "))
            user.tasks[idx].mark_complete()
            print("Task marked complete.")

        elif choice == "3":
            productivity = calculate_productivity(user.tasks)
            generate_report(user, productivity)

        elif choice == "4":
            save_data(user)
            print("Saved. Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

