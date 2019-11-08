# import tests.py


class StudentError(Exception):
    def __init__(self, string):
        pass


class DisciplineError(Exception):
    def __init__(self, string):
        pass


class GradeError(Exception):
    def __init__(self, string):
        pass


class Student:
    ids = 0

    def __init__(self, name):
        Student.ids += 1
        self._id = Student.ids
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


try:
    s = Student('123')
except StudentError as stud_err:
    print(stud_err.args[0])


class Discipline:
    ids = 0

    def __init__(self, name):
        Discipline.ids += 1
        self._id = Discipline.ids
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
