
import sqlite3

conn = sqlite3.connect('company.db')
cursor = conn.cursor()

CREATE_TABLE_USERS = """
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL
);
"""

CREATE_TABLE_TASKS = """
CREATE TABLE IF NOT EXISTS Tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    length_to_complete TEXT NOT NULL,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);
"""

cursor.execute(CREATE_TABLE_USERS)
cursor.execute(CREATE_TABLE_TASKS)

conn.commit()
conn.close()