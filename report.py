# module6_report.py
def generate_report(user, productivity):
    print("\n------ STUDY REPORT ------")
    print("Name:", user.name)
    print("Tasks:")
    for t in user.tasks:
        status = "Done" if t.completed else "Pending"
        print(f"  - {t.title} ({t.subject}) [{status}]")

    print("\nProductivity:", round(productivity, 2), "%")
    print("--------------------------")
