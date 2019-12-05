from domain.Errors import GradeError


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

    def __str__(self):
        return str(self.grade_value)

    def __dict__(self):
        grade_dict = {
            'student_id': self.student_id,
            'discipline_id': self.discipline_id,
            'grade_value': self.grade_value,
        }
        return grade_dict
