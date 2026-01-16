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
