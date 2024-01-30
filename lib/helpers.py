from db.user import User
from db.task import Task
import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()


def exit_program(): ##Add in logic for if input from user is NAN
    review = int(input("Please rate your experience with the CLI from 1 - 10:"))
    if review < 7:
        print("We hope your next time is a better experience, sorry!")
    else:
        print("We're so glad you enjoyed it, have a great day!")
    exit()

def create_user(name, department):
    cursor.execute("INSERT INTO Users (name, department) VALUES (?, ?)", (name, department))
    conn.commit()

def delete_user(user_id):
    cursor.execute("DELETE FROM Users WHERE id = ?", (user_id,))
    conn.commit()

def get_all_users(): ##Complete
    """Return all users by just their name"""
    cursor.execute("SELECT name FROM Users")
    names = cursor.fetchall()
    names = [name[0] for name in names]
    print(names)

def find_users_by_department(department): ##Complete
    cursor.execute("SELECT * FROM Users WHERE department = ?", (department,))
    user_by_department = cursor.fetchall()
    print(user_by_department)

def create_task(department, length_to_complete, description, user_id):
    cursor.execute("INSERT INTO Task (department, length_to_complete, description, user_id) VALUES (?, ?, ?, ?)",
                   (department, length_to_complete, description, user_id))
    conn.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM Task WHERE id = ?", (task_id,))
    conn.commit()

def get_all_tasks(): ##Complete
    """Return all tasks descriptions."""
    cursor.execute("SELECT description FROM Task")
    descriptions = cursor.fetchall()
    descriptions = [description[0] for description in descriptions]
    print(descriptions)


def find_tasks_by_department(department): ##Complete
    cursor.execute("SELECT * FROM Task WHERE department = ?", (department,))
    task_by_department = cursor.fetchall()
    print(task_by_department)

def find_task_by_id(task_id):##Add positional argument to cli.py
    cursor.execute("SELECT * FROM Task WHERE id = ?", (task_id,))
    task_by_id = cursor.fetchone()
    print(task_by_id)

def find_user_by_id(user_id):##Add positional argument to cli.py
    cursor.execute("SELECT * FROM Users WHERE id = ?", (user_id,))
    user_by_id = cursor.fetchone()
    print(user_by_id)