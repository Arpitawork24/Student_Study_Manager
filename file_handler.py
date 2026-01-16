def read_subjects():
    try:
        with open("data/subjects.txt", "r") as file:
            subjects = file.read().splitlines()
            return subjects
    except FileNotFoundError:
        return []


def write_subject(subject):
    with open("data/subjects.txt", "a") as file:
        file.write(subject + "\n")


def write_study_log(subject, hours):
    with open("data/study_log.txt", "a") as file:
        file.write(f"{subject},{hours}\n")


def read_study_log():
    try:
        with open("data/study_log.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []
