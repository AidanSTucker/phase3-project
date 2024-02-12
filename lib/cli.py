from helpers import (
    exit_program,
    create_user,
    delete_user,
    get_all_users,
    find_users_by_department,
    create_task,
    delete_task,
    get_all_tasks,
    find_tasks_by_department,
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
        # elif choice == "3":
        #     department = input("Enter department name: ")
        #     find_tasks_by_department(department)
        elif choice == "4":
            department = input("Enter department name: ")
            find_users_by_department(department)
        elif choice == "5": ##department, length_to_complete, description, user_id
            new_task_department = input("Enter in the department of the new task: ")
            new_task_length_to_complete = input("How long will this task take to complete: ")
            new_task_description = input("Enter in the description of this task: ")
            new_task_user_id = input("Enter in the id of the user you'd like to assign this task to: ")
            create_task(new_task_department, new_task_length_to_complete, new_task_description, new_task_user_id)
        elif choice == "6":
            task_id = input("Enter the id of the task you would like to remove: ")
            delete_task(task_id)
        elif choice == "7":
            new_user_name = input("Enter new users name: ")
            new_user_department = input("Enter new users department: ")
            create_user(new_user_name, new_user_department)
        elif choice == "8":
            user = input("Enter the name of the user you would like to remove: ")
            delete_user(user)
        elif choice == "9":
            id = input("Enter Tasks id: ")
            find_task_by_id(id)
        elif choice == "10":
            id = input("Enter Users id: ")
            find_user_by_id(id)
        elif choice == "11":
            user_id = input("Enter in the id of the user you're searching for: ")
            find_tasks_by_user(user_id)
        elif choice.isdigit():
            print("Invalid choice, please enter in a number shown on the menu: ")
        else:
            print("That was not a number, please try again: ")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View all tasks")
    print("2. View all users")
    print("3. View tasks by department")
    print("4. View users by department")
    print("5. Add new task")
    print("6. Delete task")
    print("7. Add new user")
    print("8. Delete user")
    print("9. Find task by id")
    print("10. Find user by id")
    print("11. Find all tasks owned by a user")


if __name__ == "__main__":
    main()
