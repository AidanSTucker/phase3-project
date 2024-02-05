from db.__init__ import CURSOR, CONN


class User:
    all = {}

    def __init__(self, id, department, length_to_complete, description, user_id=None):
        self.id = id
        self.department = department
        self.length_to_complete = length_to_complete
        self.user_id = user_id
        