from file_handler import read_subjects, write_subject, write_study_log

def add_subject():
    subject = input("Enter subject name: ").strip()
    if subject == "":
        print("Subject name cannot be empty.")
        return

    subjects = read_subjects()

    if subject in subjects:
        print("Subject already exists.")
    else:
        write_subject(subject)
        print("Subject added successfully.")


def log_study_hours():
    subjects = read_subjects()

    if not subjects:
        print("No subjects found. Please add a subject first.")
        return

    subject = input("Enter subject name: ").strip()

    if subject not in subjects:
        print("Subject not found. Please add it first.")
        return

    try:
        hours = float(input("Enter study hours: "))
        if hours <= 0:
            print("Hours must be greater than zero.")
            return
    except ValueError:
        print("Invalid hours entered.")
        return

    write_study_log(subject, hours)
    print("Study hours logged successfully.")



def view_progress():
    pass
