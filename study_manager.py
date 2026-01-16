from file_handler import read_subjects, write_subject

def add_subject():
    print("NEW VERSION RUNNING")
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
    pass


def view_progress():
    pass
