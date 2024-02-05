from db.__init__ import CURSOR, CONN



class Task:
    all = {}

    def __init__(self, name, department, id=None):
        self.id = id
        self.name = name
        self.department = department
        