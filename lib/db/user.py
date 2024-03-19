from db.__init__ import CURSOR, CONN
import sqlite3
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

class User:
    all = {}

    def __init__(self, name, department, id=None):
        self.id = id
        self.name = name
        self.department = department

    def __repr__(self):
        return f"| User: {self.name}, Department: {self.department} |"

    @classmethod
    def create(cls, name, department):
        user = cls(name, department)
        user.save()
        return user

    @classmethod
    def instance_from_db(cls, row):
        user = cls.all.get(row[0])
        if user:
            user.name = row[1]
            user.department = row[2]
        else:
            user = cls(row[1], row[2])
            user.id = row[0]
            cls.all[user.id] = user
        return user

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM users"
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM users WHERE id = ?"
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM users WHERE name = ?"
        row = cursor.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_department(cls, department):
        sql = "SELECT * FROM users WHERE department = ?"
        rows = cursor.execute(sql, (department,)).fetchall()
        return [cls(*row) for row in rows] if rows else None

    def save(self):
        sql = "INSERT INTO users (name, department) VALUES (?, ?)"
        cursor.execute(sql, (self.name, self.department))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = "UPDATE users SET name = ?, department = ? WHERE id = ?"
        cursor.execute(sql, (self.name, self.department, self.id))
        conn.commit()

    def delete(self):
        sql = "DELETE FROM users WHERE id = ?"
        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]
        self.id = None

    def task(self):
        from db.task import Task
        return Task.find_by_id(self.id)

