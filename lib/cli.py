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
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            tasks_menu()
        elif choice == "2":
            users_menu()
        elif choice == "3":
            manager_portal()
        elif choice.isdigit():
            print("Invalid choice, please enter a valid option number.")
        else:
            print("Invalid input, please enter a number corresponding to the menu option.")

def main_menu():
    print("#######################################")
    print("#            Main Menu                #")
    print("#######################################")
    print("#  0. Exit the program                #")
    print("#  1. Tasks                           #")
    print("#  2. Users                           #")
    print("#  3. Manager Portal                  #")
    print("#######################################")

def manager_portal():
    manager_code = input("Enter manager's code: ")
    if manager_code == '123':
        while True:
            print("#######################################")
            print("#          Manager Portal             #")
            print("#######################################")
            print("#  0. Go back to main menu           #")
            print("#  1. View all users                 #")
            print("#  2. View users by department       #")
            print("#  3. Add new user                   #")
            print("#  4. Delete user                    #")
            print("#  5. Find user by id                #")
            print("#  6. Delete task                    #")
            print("#  7. Create task                    #")
            print("#  8. View tasks by user             #")
            print("#######################################")
            choice = input("> ")
            if choice == "0":
                break
            elif choice == "1":
                get_all_users()
            elif choice == "2":
                find_users_by_department()
            elif choice == "3":
                create_user()
            elif choice == "4":
                delete_user()
            elif choice == "5":
                find_user_by_id()
            elif choice == "6":
                delete_task()
            elif choice == "7":
                create_task()
            elif choice == "8":
                find_tasks_by_user()
            elif choice.isdigit():
                print("Invalid choice, please enter a valid option number.")
            else:
                print("Invalid input, please enter a number corresponding to the menu option.")
    else:
        print("Access denied")

def tasks_menu():
    while True:
        print("#######################################")
        print("#            Tasks Menu               #")
        print("#######################################")
        print("#  0. Go back to main menu           #")
        print("#  1. View all tasks                 #")
        print("#  2. Find a specific task           #")
        print("#  3. View my tasks                  #")
        print("#######################################")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            get_all_tasks()
        elif choice == "2":
            find_task_by_id()
        elif choice == "3":
            active_tasks_menu()
        elif choice.isdigit():
            print("Invalid choice, please enter a valid option number.")
        else:
            print("Invalid input, please enter a number corresponding to the menu option.")

def active_tasks_menu():
    while True:
        print("\nActive Tasks Menu:")
        find_tasks_by_user()
        print("1. Assign new task")
        print("2. Mark a task complete")
        print("0. Go back to tasks menu")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            create_task()
        elif choice == "2":
            delete_task()
        elif choice.isdigit():
            print("Invalid choice, please enter a valid option number.")
        else:
            print("Invalid input, please enter a number corresponding to the menu option.")

def users_menu():
    while True:
        print("#######################################")
        print("#            Users Menu               #")
        print("#######################################")
        print("#  0. Go back to main menu           #")
        print("#  1. View all users                 #")
        print("#  2. View your team members         #")
        print("#  3. Find user by id                #")
        print("#######################################")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            get_all_users()
        elif choice == "2":
            find_users_by_department()
        elif choice == "3":
            find_user_by_id()
        elif choice.isdigit():
            print("Invalid choice, please enter a valid option number.")
        else:
            print("Invalid input, please enter a number corresponding to the menu option.")

if __name__ == "__main__":
    main()
