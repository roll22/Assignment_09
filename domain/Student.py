import uuid

from domain.Errors import StudentError


class Student:

    def __init__(self, name):
        self._id = uuid.uuid1().hex
        self.name = name

    @staticmethod
    def create_from_data(name, id):
        obj = Student(name)
        obj._id = id
        return obj

    def get_id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise StudentError('Name must be string')
        if not name.isalpha():
            raise StudentError('Name must be string')
        self._name = name

    def __str__(self):
        return self.name

    def __dict__(self):
        stud_dict = {
            '_id': self._id,
            'name': self.name
        }
        return stud_dict
