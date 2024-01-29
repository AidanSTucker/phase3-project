from db.user import User
from db.task import Task


def exit_program():
    print("Goodbye!")
    exit()

def create_user(name, department):
    return User.create(name=name, department=department)

def delete_user(user_id):
    User.get(User.id == user_id).delete_instance()

def get_all_users():
    return User.select()

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
    tasks = Task.get_all()
    for task in tasks:
        print(task)
    

def find_tasks_by_department(department):
    return Task.select().where(Task.department == department)

def find_task_by_id(task_id):
    return Task.get(Task.id == task_id)

def find_user_by_id(user_id):
    return User.get(User.id == user_id)