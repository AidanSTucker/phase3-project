from db.__init__ import CURSOR, CONN
import sqlite3
conn = sqlite3.connect('company.db')
cursor = conn.cursor()


class Task:
    all = {}

    def __init__(self, department, length_to_complete, description, user_id, id=None):
        self.id = id
        self.department = department
        self.length_to_complete = length_to_complete
        self.description = description
        self.user_id = user_id

    def __repr__(self):
        return f"<Task {self.id}: {self.description}, Department: {self.department}, User ID: {self.user_id}>"

    @classmethod
    def create(cls, department, length_to_complete, description, user_id):
        task = cls(department, length_to_complete, description, user_id)
        task.save()
        return task

    @classmethod
    def instance_from_db(cls, row):
        task = cls.all.get(row[0])
        if task:
            task.department = row[1]
            task.length_to_complete = row[2]
            task.description = row[3]
            task.user_id = row[4]
        else:
            task = cls(row[1], row[2], row[3], row[4])
            task.id = row[0]
            cls.all[task.id] = task
        return task

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM Task"
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM Task WHERE id = ?"
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_department(cls, department):
        sql = "SELECT * FROM Task WHERE department = ?"
        rows = cursor.execute(sql, (department,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_user_id(cls, user_id):
        sql = "SELECT * FROM Task WHERE user_id = ?"
        rows = cursor.execute(sql, (user_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    def save(self):
        sql = "INSERT INTO Task (department, length_to_complete, description, user_id) VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (self.department, self.length_to_complete, self.description, self.user_id))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = "UPDATE Task SET department = ?, length_to_complete = ?, description = ?, user_id = ? WHERE id = ?"
        cursor.execute(sql, (self.department, self.length_to_complete, self.description, self.user_id, self.id))
        conn.commit()

    def delete(self):
        sql = "DELETE FROM Task WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]
        self.id = None
