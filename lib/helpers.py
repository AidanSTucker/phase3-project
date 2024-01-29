from db.user import User
from db.task import Task
import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()


def exit_program():
    review = int(input("Please rate your experience with the CLI from 1 - 10:"))
    if review < 7:
        print("We hope your next time is a better experience, sorry!")
    else:
        print("We're so glad you enjoyed it, have a great day!")
    exit()

def create_user(name, department):
    return User.create(name=name, department=department)

def delete_user(user_id):
    User.get(User.id == user_id).delete_instance()

def get_all_users():
    """Return all users by just their name"""
    cursor.execute("SELECT name FROM Users")
    names = cursor.fetchall()
    names = [name[0] for name in names]
    print(names)

def find_users_by_department(department):
    return User.select().where(User.department == department)

# ORM methods for Task
def create_task(department, length_to_complete, description, user_id):
    return Task.create(
        department=department,
        length_to_complete=length_to_complete,
        description=description,
        user=user_id
    )

def delete_task(task_id):
    Task.get(Task.id == task_id).delete_instance()

def get_all_tasks():
    """Return all tasks descriptions."""
    cursor.execute("SELECT description FROM Task")
    descriptions = cursor.fetchall()
    descriptions = [description[0] for description in descriptions]
    print(descriptions)

    
    

def find_tasks_by_department(department):
    return Task.select().where(Task.department == department)

def find_task_by_id(task_id):
    return Task.get(Task.id == task_id)

def find_user_by_id(user_id):
    return User.get(User.id == user_id)