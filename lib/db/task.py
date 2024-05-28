from db.user import User
import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()
## lists, list comprehension, psuedocoding, debugging tools, how to call a class method, finish up find_by_length function, add to menuing

class Task:
    all = {}

    def __init__(self, length_to_complete, description, user_id, id=None):
        self.id = id
        self.length_to_complete = length_to_complete
        self.description = description
        self.user_id = user_id


    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if len(value) < 10:
            raise ValueError("description must be at least 10 characters long.")
        self._description = value

    @property
    def length_to_complete(self):
        return self._length_to_complete
    
    @length_to_complete.setter
    def length_to_complete(self, value):
        if len(value) < 4:
            raise ValueError("Please include the time metric for the length to complete!")
        self._length_to_complete = value
        
    def __repr__(self):
        return f"| Task {self.description}, Length to complete: {self.length_to_complete} |"
    
    ## New method as discussed with Mr. Parish!
    @classmethod
    def find_by_length(cls, max_length):
        sql = "SELECT * FROM Task WHERE LENGTH(description) <= ?"
        rows = cursor.execute(sql, (max_length,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else []

    
    @classmethod
    def create(cls, description, length_to_complete, user_id):
        task = cls(description, length_to_complete, user_id)
        task.save()
        return task

    @classmethod
    def instance_from_db(cls, row):
        task = cls.all.get(row[0])
        if task:
            task.length_to_complete = row[1]
            task.description = row[2]
            task.user_id = row[3]
        else:
            task = cls(row[1], row[2], row[3])
            task.id = row[0]
            cls.all[task.id] = task
        return task

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM Task"
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_description(cls, description):
        sql = "SELECT * FROM Task WHERE description = ?"
        row = cursor.execute(sql, (description,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_user_id(cls, user_id):
        sql = "SELECT * FROM Task WHERE user_id = ?"
        rows = cursor.execute(sql, (user_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM Task WHERE id = ?"
        rows = cursor.execute(sql, (id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    def save(self):
        sql = "INSERT INTO Task (length_to_complete, description, user_id) VALUES (?, ?, ?)"
        cursor.execute(sql, (self.length_to_complete, self.description, self.user_id))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = "UPDATE Task SET length_to_complete = ?, description = ?, user_id = ? WHERE id = ?"
        cursor.execute(sql, (self.length_to_complete, self.description, self.user_id, self.id))
        conn.commit()

    def delete(self):
        sql = "DELETE FROM Task WHERE description = ?"
        cursor.execute(sql, (self.description,))
        conn.commit()

    def user(self):
        return User.find_by_id(self.user_id)
