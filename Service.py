from Domain import Student, Discipline
from repository import StudentRepository, DisciplineRepository, GradeRepository, Grade


class IOErr(Exception):
    pass


class StudentService:
    def __init__(self):
        self._repo = StudentRepository()

    def add(self, name):
        """
        Makes validations, creates the object and calls the repo Add
        :raises: IOErr
        """
        if not name.isalpha():
            raise IOErr("name must be literal")
        self._repo.add(Student(name))

    def remove(self, name):
        """
        Makes validations, finds the index and calls the repo remove
        Calls the GradeServices repo remove
        :raises: IOErr
        """
        if not name.isalpha():
            raise IOErr("name must be literal")
        _list = self._repo.get_list()
        for idx, student in enumerate(_list):
            if student.name == name:
                stud_id = student.get_id()
                self._repo.remove(index=idx)
                return stud_id
                # TODO take care of teests coverage

    def count_occurence(self, name):
        """
        Counts the occurences of a name in the list
        :param name:
        :return: count<int>
        """
        _list = self._repo.get_list()
        count = 0
        for idx, student in enumerate(_list):
            if student.name == name:
                count += 1
        return count

    def update(self, name, new_name):
        """
        Updates the name of the student with a new name
        :param name:
        :param new_name:
        :return:
        """
        _list = self._repo.get_list()
        for idx, student in enumerate(_list):
            if student.name == name:
                student.name = new_name

    def display(self):
        return self._repo.get_list()


class DisciplineService:
    def __init__(self):
        self._repo = DisciplineRepository()

    def add(self, name):
        """
        Makes validations, creates the object and calls the repo Add
        :raises: IOErr
        """
        if not name.isalpha():
            raise IOErr("name must be literal")
        self._repo.add(Discipline(name))

    def remove(self, name):
        """
        Makes validations, finds the index and calls the repo remove
        Calls the GradeServices repo remove
        :raises: IOErr
        """
        if not name.isalpha():
            raise IOErr("name must be literal")
        _list = self._repo.get_list()
        for idx, discipline in enumerate(_list):
            if discipline.name == name:
                disc_id = discipline.get_id()
                self._repo.remove(index=idx)
                return disc_id
                # TODO REMOVE GRADES! using disc_id
                # take care of teests coveragedf

    def count_occurence(self, name):
        """
        Counts the occurences of a name in the list
        :param name:
        :return: count<int>
        """
        _list = self._repo.get_list()
        count = 0
        for idx, discipline in enumerate(_list):
            if discipline.name == name:
                count += 1
        return count

    def update(self, name, new_name):
        """
        Updates the name of the discipline with a new name
        :param name:
        :param new_name:
        :return:
        """
        _list = self._repo.get_list()
        for idx, discipline in enumerate(_list):
            if discipline.name == name:
                discipline.name = new_name

    def display(self):
        return self._repo.get_list()


class GradeService:
    def __init__(self):
        self._repo = GradeRepository()

    def add(self, discipline_id, student_id, grades):
        """
        Creates the object and calls the repo Add
        :raises: IOErr
        """
        for grade in grades:
            self._repo.add(Grade(student_id, discipline_id, grade))
            # for debugging
            for obj in self._repo.get_list():
                print(obj.student_id, obj.discipline_id, obj.grade_value)

    def remove_by_student_id(self, stud_id):
        _list = self._repo.get_list()
        to_delete = []
        for idx, grade in enumerate(_list):
            if grade.student_id == stud_id:
                to_delete.append(idx)
        for offset, idx in enumerate(to_delete):
            idx -= offset
            self._repo.remove(idx)

    def remove_by_discipline_id(self, disc_id):
        _list = self._repo.get_list()
        to_delete = []
        for idx, grade in enumerate(_list):
            if grade.student_id == disc_id:
                to_delete.append(idx)
        for offset, idx in enumerate(to_delete):
            idx -= offset
            self._repo.remove(idx)


class Service:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
