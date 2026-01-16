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
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
