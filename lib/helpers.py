from db.user import User
from db.task import Task
import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()


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


def create_user(name, department): ##Complete
    cursor.execute("INSERT INTO Users (name, department) VALUES (?, ?)", (name, department))
    conn.commit()
    

def delete_user(name): ##Complete
    cursor.execute("DELETE FROM Users WHERE name = ?", (name,))
    conn.commit()

def get_all_users(): ##Complete
    """Return all users by just their name"""
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    print("--------------------------")
    print("All Users:\n")
    for user in users:
        print("- Name: ", user[1])
        print("- Department: ", user[2])
        print("- User Id: ", user[0])
        print("")
    print("--------------------------")

def find_users_by_department(department):
    cursor.execute("SELECT * FROM Users WHERE department = ?", (department,))
    users = cursor.fetchall()
    if users:
        print(f"All Users in Department '{department}':\n")
        print("--------------------------")
        for user in users:
            print("- Name: ", user[1])
            print("- User Id: ", user[0])
            print("")
        print("--------------------------")
    else:
        print(f"No users found in department '{department}'.")

def create_task(department, length_to_complete, description, user_id):
    cursor.execute("INSERT INTO Task (department, length_to_complete, description, user_id) VALUES (?, ?, ?, ?)",
                   (department, length_to_complete, description, user_id))
    conn.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM Task WHERE id = ?", (task_id,))
    conn.commit()

def get_all_tasks():
    """Return all tasks descriptions."""
    cursor.execute("SELECT * FROM Task")
    tasks = cursor.fetchall()
    print("--------------------------")
    print("All Tasks:\n")
    for task in tasks:
        print("- Description:", task[3])
        print("  - Length to Complete:", task[2])
        print("  - Department:", task[1])
        print("  - User id assigned to:", task[4])
        print("")
    print("--------------------------")


def find_tasks_by_department(department):
    cursor.execute("SELECT * FROM Task WHERE department = ?", (department,))
    tasks = cursor.fetchall()
    if tasks:
        print(f"All Tasks in Department '{department}':\n")
        print("--------------------------")
        for task in tasks:
            print("- Description:", task[3])
            print("  - Length to Complete:", task[2])
            print("  - User ID Assigned:", task[4])
            print("")
        print("--------------------------")
    else:
        print(f"No tasks found in department '{department}'.")

def find_task_by_id(task_id):
    cursor.execute("SELECT * FROM Task WHERE id = ?", (task_id,))
    task_by_id = cursor.fetchone()
    if task_by_id:
        print("--------------------------")
        print("- Description:", task_by_id[3])
        print("  - Length to Complete:", task_by_id[2])
        print("  - Department:", task_by_id[1])
        print("  - User id assigned to:", task_by_id[4])
        print("")
        print("--------------------------")
    else:
        print("No task found with the specified ID.")

def find_user_by_id(user_id):
    cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id,))
    user_by_id = cursor.fetchone()
    if user_by_id:
        print("--------------------------")
        print("- Name: ", user_by_id[1])
        print("- Department: ", user_by_id[2])
        print("")
        print("--------------------------")
    else:
        print("No user found with the specified ID.")


def find_tasks_by_user(user_id):
    cursor.execute("SELECT * FROM Task WHERE user_id = ?", (user_id,))
    tasks = cursor.fetchall()
    if tasks:
        print("--------------------------")
        for task in tasks:
            print("- Description:", task[3])
            print("  - Length to Complete:", task[2])
            print("")
        print("--------------------------")
    else:
        print("No tasks found for the specified user ID.")