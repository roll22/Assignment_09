from Domain import Student, Discipline
from repository import StudentRepository, DisciplineRepository, GradeRepository, Grade
import re


class IOErr(Exception):
    pass


class StudentService:
    def __init__(self):
        self._repo = StudentRepository()

    def add_obj(self, obj):
        self._repo.add(obj)

    def add(self, name):
        """
        Makes validations, creates the object and calls the repo Add
        :raises: IOErr
        """
        if not name.isalpha():
            raise IOErr("name must be literal")
        obj = Student(name)
        self._repo.add(obj)
        return obj

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
                return student

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
                break
        return name, new_name

    def display(self):
        return self._repo.get_list()

    def search(self, match):
        match = '^' + match
        returns = []
        _list = self._repo.get_list()
        for idx, student in enumerate(_list):
            if re.search(match, student.name, re.IGNORECASE):
                returns.append([student.name, student.get_id()])
        return returns


class DisciplineService:
    def __init__(self):
        self._repo = DisciplineRepository()

    def add_obj(self, obj):
        self._repo.add(obj)

    def add(self, name):
        """
        Makes validations, creates the object and calls the repo Add
        :raises: IOErr
        """
        if not name.isalpha():
            raise IOErr("name must be literal")
        obj = Discipline(name)
        self._repo.add(obj)
        return obj

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
                return discipline

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
                break
        return name, new_name

    def display(self):
        return self._repo.get_list()

    def search(self, match):
        match = '^' + match
        returns = []
        _list = self._repo.get_list()
        for idx, discipline in enumerate(_list):
            if re.search(match, discipline.name, re.IGNORECASE) is not None:
                returns.append([discipline.name, discipline.get_id()])
        return returns


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


class Service:

    def __init__(self, student_serv, discipline_serv, grade_serv):
        self.student_service = student_serv
        self.discipline_service = discipline_serv
        self.grade_service = grade_serv
        self.undo_stack = []
        self.redo_stack = []
        self.flag = False

    def initialize_repos(self):
        names = [
            "Andrei",
            "Raul",
            "Flaviu",
            "Mirel",
            "Marcel",
            "Calutz",
            "Dellutz",
            "Kronos",
            "Irina",
            "Balaur",
        ]
        for name in names:
            self.student_service.add(name)
        disciplines = [
            "Algebra",
            "Analiza",
            "FP",
            "ASC",
            "Logica",
            "Geometrie",
            "Sisteme",
            "Cuantica",
            "BazedeDate",
            "Fotografie",
        ]
        for discipline in disciplines:
            self.discipline_service.add(discipline)

        for x in range(20):
            import random
            random_student = self.student_service.display()[random.randint(0, 9)].get_id()
            random_discipline = self.discipline_service.display()[random.randint(0, 9)].get_id()
            random_grade = random.randint(1, 10)
            self.grade_service.add(discipline_id=random_discipline, student_id=random_student, grades=[random_grade])

    def failing(self):
        failed_students = []
        _student_list = self.student_service.display()
        _discipline_list = self.discipline_service.display()
        _grade_list = self.grade_service.display()
        for student in _student_list:
            stud_id = student.get_id()
            for discipline in _discipline_list:
                disc_id = discipline.get_id()
                sum_ = 0
                count_ = 0
                for grade in _grade_list:
                    if grade.student_id == stud_id and grade.discipline_id == disc_id:
                        sum_ += grade.grade_value
                        count_ += 1
                if count_ == 0:
                    continue
                if sum_ / count_ < 5:
                    if student.name not in failed_students:
                        failed_students.append([student, discipline, sum_ / count_])
        return failed_students

    def best_stats(self):
        students = []
        _student_list = self.student_service.display()
        _discipline_list = self.discipline_service.display()
        _grade_list = self.grade_service.display()
        for student in _student_list:
            stud_id = student.get_id()
            averages = []
            for discipline in _discipline_list:
                disc_id = discipline.get_id()
                sum_ = 0
                count_ = 0
                for grade in _grade_list:
                    if grade.student_id == stud_id and grade.discipline_id == disc_id:
                        sum_ += grade.grade_value
                        count_ += 1
                if count_ != 0:
                    averages.append(sum_ / count_)
            if len(averages) == 0:
                continue
            general_average = sum(averages) / len(averages)
            students.append([student, general_average])
        return sorted(students, key=lambda item: item[1], reverse=True)

    def discipline_stats(self):
        _student_list = self.student_service.display()
        _discipline_list = self.discipline_service.display()
        _grade_list = self.grade_service.display()
        students_averages = []
        for student in _student_list:
            stud_id = student.get_id()
            averages = []
            for discipline in _discipline_list:
                disc_id = discipline.get_id()
                sum_ = 0
                count_ = 0
                for grade in _grade_list:
                    if grade.student_id == stud_id and grade.discipline_id == disc_id:
                        sum_ += grade.grade_value
                        count_ += 1
                if count_ == 0:
                    continue
                averages.append([discipline, sum_ / count_])
            students_averages.extend(averages)
        final_averages = []
        for discipline in _discipline_list:
            sum_ = 0
            count_ = 0
            for list_of_avgs in students_averages:
                if discipline.get_id() == list_of_avgs[0].get_id():
                    sum_ += list_of_avgs[1]
                    count_ += 1
            if count_ != 0:
                final_averages.append([discipline, sum_ / count_])
        return sorted(final_averages, key=lambda avg: avg[1], reverse=True)

    def stack_care(self, _list):
        if self.flag:
            self.redo_stack.clear()
        self.undo_stack.append(_list)
        self.flag = False

    def undo(self):
        func_map = {
            self.student_service.add: self.remove_student,
            self.discipline_service.add: self.remove_discipline,
            self.student_service.update: self.update_student_undo,
            self.discipline_service.update: self.update_discipline_undo,
            self.grade_service.add: self.remove_grade,
            self.student_service.remove: self.add_student,
            self.discipline_service.remove: self.add_discipline,
            self.grade_service.remove_by_student_id: self.add_multiple_grades,
            self.grade_service.remove_by_discipline_id: self.add_multiple_grades,

        }

        if len(self.undo_stack) == 0:
            raise IOErr("Out of undos!")
        _list = self.undo_stack.pop(-1)
        for operation in _list:
            func = func_map[operation[0]]
            obj = operation[1]
            func(obj)
        self.redo_stack.append(_list)
        self.flag = True

    def redo(self):
        func_map = {
            self.student_service.add: self.add_student,
            self.discipline_service.add: self.add_discipline,
            self.student_service.update: self.update_student_redo,
            self.discipline_service.update: self.update_discipline_redo,
            self.grade_service.add: self.add_grade,
            self.student_service.remove: self.remove_student,
            self.discipline_service.remove: self.remove_discipline,
            self.grade_service.remove_by_student_id: self.remove_multiple_grades,
            self.grade_service.remove_by_discipline_id: self.remove_multiple_grades,

        }
        if len(self.redo_stack) == 0:
            raise IOErr("Out of redos!")
        _list = self.redo_stack.pop(-1)
        for operation in _list:
            func = func_map[operation[0]]
            obj = operation[1]
            func(obj)

        self.undo_stack.append(_list)

    # custom functions
    # they call the functions from the service, they only edit the params

    def add_student(self, obj):
        self.student_service.add_obj(obj)

    def remove_student(self, obj):
        self.student_service.remove(obj.name)

    def add_discipline(self, obj):
        self.discipline_service.add_obj(obj)

    def remove_discipline(self, obj):
        self.discipline_service.remove(obj.name)

    def update_student_undo(self, obj):
        self.student_service.update(obj[1], obj[0])

    def update_student_redo(self, obj):
        self.student_service.update(obj[0], obj[1])

    def update_discipline_undo(self, obj):
        self.discipline_service.update(obj[1], obj[0])

    def update_discipline_redo(self, obj):
        self.discipline_service.update(obj[0], obj[1])

    def add_grade(self, obj):
        self.grade_service.add(obj[0], obj[1], obj[2])

    def remove_grade(self, obj):
        for x in range(len(obj[2])):
            self.grade_service.remove(obj[0], obj[1], obj[2][x])

    def add_multiple_grades(self, obj):
        for grade in obj:
            self.grade_service.add(grade.discipline_id, grade.student_id, [grade.grade_value])

    def remove_multiple_grades(self, obj):
        for grade in obj:
            self.grade_service.remove(grade.discipline_id, grade.student_id, grade.grade_value)

