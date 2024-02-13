from helpers import (
    exit_program,
    create_user,
    delete_user,
    get_all_users,
    find_users_by_department,
    create_task,
    delete_task,
    get_all_tasks,
    find_task_by_id,
    find_user_by_id,
    find_tasks_by_user
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_all_tasks()
        elif choice == "2":
            get_all_users()
        elif choice == "3":
            find_users_by_department()
        elif choice == "4": 
            create_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            create_user()
        elif choice == "7":
            delete_user()
        elif choice == "8":
            find_task_by_id()
        elif choice == "9":
            find_user_by_id()
        elif choice == "10":
            find_tasks_by_user()
        elif choice.isdigit():
            print("Invalid choice, please enter in a number shown on the menu: ")
        else:
            print("That was not a number, please try again: ")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View all tasks")
    print("2. View all users")
    print("3. View users by department")
    print("4. Add new task")
    print("5. Delete task")
    print("6. Add new user")
    print("7. Delete user")
    print("8. Find task by id")
    print("9. Find user by id")
    print("10. Find your active tasks")


if __name__ == "__main__":
    main()
