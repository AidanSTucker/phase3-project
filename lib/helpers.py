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

def create_user():
    name = input("Enter new users name: ")
    department = input("Enter new users department: ")
    try:
        user = User.create(name, department)
        print(f"Success: {user}")
    except Exception as exc:
        print("Error creating user: ", exc)

def delete_user():
    name = input("Enter the name of the user you would like to remove: ")
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
        print("")
    print("--------------------------")

def find_users_by_department(): 
    department = input("Enter department name: ")
    users = User.find_by_department(department)
    if users:
        print(f"Your coworkers in '{department}':\n")
        print("--------------------------")
        for user in users:
            print("- Name: ", user.department)
            print("")
        print("--------------------------")
    else:
        print(f"No users found in department '{department}'.")

def create_task():
    description = input("Enter the description of the task: ")
    length_to_complete = input("Enter the length to complete: ")
    assigned_user_name = input("Enter the name of the user to assign the task to: ")

    assigned_user = User.find_by_name(assigned_user_name)
    if assigned_user:
        try:
            task = Task.create(length_to_complete, description, assigned_user.id)
            print(f"Task created: {task}")
        except Exception as exc:
            print("Error creating task: ", exc)
    else:
        print(f"No user found with the name '{assigned_user_name}'. Task not created.")


def delete_task():
    description = input("Enter the description of the task you would like to remove: ")
    task = Task.find_by_description(description)
    if task:
        task.delete()
        print(f"Task '{description}' deleted")
    else:
        print(f"Task '{description}' not found")

def get_all_tasks():
    tasks = Task.get_all()
    for task in tasks:
        print(task)

def find_task_by_description():
    task_description = input("Enter Task Title: ")
    task = Task.find_by_description(task_description)
    
    if task:
        user_name = task.user().name  # Retrieve the name of the user associated with the task
        print("--------------------------")
        print("- Title:", task.description)
        print("  - Length to Complete:", task.length_to_complete)
        print("  - User assigned to:", user_name)  # Print the name of the user
        print("--------------------------")
    else:
        print("No task found with that title.")

def find_tasks_by_user():
    user_name = input("Enter name: ")
    user = User.find_by_name(user_name)
    if user:
        tasks = user.tasks()
        if tasks:
            print("--------------------------")
            for task in tasks:
                print("- Description:", task.description)
                print("  - Length to Complete:", task.length_to_complete)
                print("  - User assigned to:", user_name)
                print("")
            print("--------------------------")
        else:
            print("No tasks found associated with that user.")
    else:
        print("Name not found.")
## call User.tasks -> all set!
## line 107 can be commented our / implemented into one line on 108 -> removed!