import uuid

from domain.Errors import DisciplineError


class Discipline:

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
            raise DisciplineError('Name must be string')
        if not name.isalpha():
            raise DisciplineError('Name must be string')
        self._name = name

    def __str__(self):
        return self.name

    @classmethod
    def create_from_data(cls, name, id):
        obj = Discipline(name)
        obj._id = id
        return obj

    def __dict__(self):
        disc_dict = {
            '_id': self._id,
            'name': self.name
        }
        return disc_dict
