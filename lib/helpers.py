from db.user import User
from db.task import Task

def exit_program():
    while True:
        try:
            review = int(input("Please rate your experience with the CLI from 1 - 10: "))
            if 1 <= review <= 10:
                if review < 7:
                    print("We hope your next time is a better experience, sorry!")
                else:
                    print("We're so glad you enjoyed it, have a great day!")
                exit()  # Exit the program after printing the message
            else:
                print("Error: Please enter a number between 1 and 10.")
        except ValueError:
            print("Error: Value entered is not a number, please try again.")

def create_user(name, department):
    try:
        user = User.create(name, department)
        print(f"Success: {user}")
    except Exception as exc:
        print("Error creating user: ", exc)

def delete_user(name):
    if user := User.find_by_name(name):
        user.delete()
        print(f"User {name} deleted")
    else:
        print(f"User {name} not found")

def get_all_users():
    users = User.get_all()
    print("--------------------------")
    print("All Users:\n")
    for user in users:
        print("- Name: ", user.name)
        print("- Department: ", user.department)
        print("- User Id: ", user.id)
        print("")
    print("--------------------------")

def find_users_by_department(department):     ## --> Needs work
    users = User.find_by_department(department)
    if users:
        print(f"All Users in Department '{department}':\n")
        print("--------------------------")
        for user in users:
            print("- Name: ", user.name)
            print("- User Id: ", user.id)
            print("")
        print("--------------------------")
    else:
        print(f"No users found in department '{department}'.")

def create_task(department, length_to_complete, description, user_id):
    try:
        task = Task.create(department, length_to_complete, description, user_id)
        print(f"Task created: {task}")
    except Exception as exc:
        print("Error creating task: ", exc)

def delete_task(task_id):
    if task := Task.find_by_id(task_id):
        task.delete()
        print(f"Task {task_id} deleted")
    else:
        print(f"Task {task_id} not found")

def get_all_tasks():
    tasks = Task.get_all()
    for task in tasks:
        print(task)

def find_tasks_by_department(department):
    tasks = Task.find_by_department(department)
    if tasks:
        print(f"All Tasks in Department '{department}':\n")
        print("--------------------------")
        for task in tasks:
            print("- Description:", task.description)
            print("  - Length to Complete:", task.length_to_complete)
            print("  - User ID Assigned:", task.user_id)
            print("")
        print("--------------------------")
    else:
        print(f"No tasks found in department '{department}'.")

def find_task_by_id(task_id):
    if task := Task.find_by_id(task_id):
        print("--------------------------")
        print("- Description:", task.description)
        print("  - Length to Complete:", task.length_to_complete)
        print("  - Department:", task.department)
        print("  - User id assigned to:", task.user_id)
        print("")
        print("--------------------------")
    else:
        print("No task found with the specified ID.")

def find_user_by_id(user_id):
    if user := User.find_by_id(user_id):
        print("--------------------------")
        print("- Name: ", user.name)
        print("- Department: ", user.department)
        print("")
        print("--------------------------")
    else:
        print("No user found with the specified ID.")

def find_tasks_by_user(user_id):
    tasks = Task.find_by_user_id(user_id)
    if tasks:
        print("--------------------------")
        for task in tasks:
            print("- Description:", task.description)
            print("  - Length to Complete:", task.length_to_complete)
            print("")
        print("--------------------------")
    else:
        print("No tasks found for the specified user ID.")
