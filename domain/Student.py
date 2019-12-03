import uuid

from domain.Errors import StudentError


class Student:

    def __init__(self, name):
        self._id = uuid.uuid1().hex
        self.name = name

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

    """ `
    def student_to_dict(self):
        stud_dict = {
            '_id': self._id,
            'value': self.name
        }
    """