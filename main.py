from study_manager import add_subject
from study_manager import log_study_hours
from study_manager import view_progress

def show_menu():
    print("\n--- Student Study Manager ---")
    print("1. Add Subject")
    print("2. Log Study Hours")
    print("3. View Progress")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_subject()
        elif choice == "2":
            log_study_hours()
        elif choice == "3":
            view_progress()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
