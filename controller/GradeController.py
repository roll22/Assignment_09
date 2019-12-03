from domain.Grade import Grade
from repository_module.GradeRepository import GradeRepository


class GradeService:
    def __init__(self):
        self._repo = GradeRepository()

    def store(self, discipline_id, student_id, grades):
        """
        Creates the object and calls the repo Add
        :raises: IOErr
        """
        for grade in grades:
            self._repo.store(Grade(student_id, discipline_id, grade))

    def remove(self, discipline_id, student_id, grade_val):
        _list = self._repo.get_list()
        returnable = None
        for idx, grade in enumerate(_list):
            if grade.student_id == student_id and grade.discipline_id == discipline_id and grade.grade_value == grade_val:
                returnable = grade
                self._repo.remove(idx)
        return returnable

    def remove_by_student_id(self, stud_id):
        _list = self._repo.get_list()
        to_delete = []
        for idx, grade in enumerate(_list):
            if grade.student_id == stud_id:
                to_delete.append([idx, grade])
        for offset, idx in enumerate(to_delete):
            self._repo.remove(idx[0] - offset)
        returnable = list(x[1] for x in to_delete)
        return returnable

    def remove_by_discipline_id(self, disc_id):
        _list = self._repo.get_list()
        to_delete = []
        for idx, grade in enumerate(_list):
            if grade.discipline_id == disc_id:
                to_delete.append([idx, grade])
        for offset, idx in enumerate(to_delete):
            self._repo.remove(idx[0] - offset)
        returnable = list(x[1] for x in to_delete)
        return returnable

    def display(self):
        return self._repo.get_list()