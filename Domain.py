# import tests.py
import uuid


class ServiceErr(Exception):
    pass


class StudentError(ServiceErr):
    def __init__(self, string):
        pass


class DisciplineError(ServiceErr):
    def __init__(self, string):
        pass


class GradeError(ServiceErr):
    def __init__(self, string):
        pass


class Student:

    def __init__(self, name):
        self._id = uuid.uuid1().hex
        self.name = name

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
    """
    def student_to_dict(self):
        stud_dict = {
            '_id': self._id,
            'value': self.name
        }
    """
class Discipline:

    def __init__(self, name):
        self._id = uuid.uuid1().hex
        self.name = name

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


class Grade:

    def __init__(self, student_id, discipline_id, grade_value):
        self.student_id = student_id
        self.discipline_id = discipline_id
        self.grade_value = grade_value

    @property
    def grade_value(self):
        return self._grade_value

    @grade_value.setter
    def grade_value(self, grade_value):
        if type(grade_value) != int:
            if type(grade_value) == str:
                if grade_value.isdigit():
                    grade_value = int(grade_value)
                    if 1 <= grade_value <= 10:
                        self._grade_value = grade_value
                    else:
                        raise GradeError('Grade must be between 1 and 10')
            else:
                raise GradeError('Grade must be an integer')
        if 1 <= grade_value <= 10:
            self._grade_value = grade_value
        else:
            raise GradeError('Grade must be between 1 and 10')

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, stud_id):
        self._student_id = stud_id

    @property
    def discipline_id(self):
        return self._discipline_id

    @discipline_id.setter
    def discipline_id(self, disc_id):
        self._discipline_id = disc_id
