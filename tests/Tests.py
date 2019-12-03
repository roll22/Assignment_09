import unittest

from controller.MainController import Service
from controller.GradeController import GradeService
from controller.DisciplineController import DisciplineService
from controller.StudentController import StudentService
from controller.IOErr import IOErr
from repository_module.Repository import Repository
from repository_module.StudentRepository import StudentRepository
from repository_module.DisciplineRepository import DisciplineRepository
from repository_module.GradeRepository import GradeRepository
from repository_module.RepoErr import RepoErr
from domain.Grade import Grade
from domain.Discipline import Discipline
from domain.Student import Student
from domain.Errors import StudentError, DisciplineError, GradeError


class DomainTest(unittest.TestCase):
    def test_Student(self):
        obj = Student('marcel')
        self.assertEqual(obj.name, 'marcel')
        self.assertIsNotNone(obj._id)
        with self.assertRaises(StudentError):
            obj.name = 123
        with self.assertRaises(StudentError):
            obj.name = '123'
        self.assertEqual(obj.get_id(), obj._id)
        self.assertEqual(obj.__str__(), obj.name)

    def test_Discipline(self):
        obj = Discipline('Disciplina')
        self.assertEqual(obj.name, 'Disciplina')
        self.assertIsNotNone(obj._id)
        with self.assertRaises(DisciplineError):
            obj.name = 123
        with self.assertRaises(DisciplineError):
            obj.name = '123'
        self.assertEqual(obj.get_id(), obj._id)
        self.assertEqual(obj.__str__(), obj.name)

    def test_Grade(self):
        obj = Grade('stud_id', 'disc_id', 5)
        self.assertEqual(obj.student_id, 'stud_id')
        self.assertEqual(obj.discipline_id, 'disc_id')
        self.assertEqual(obj.grade_value, 5)
        with self.assertRaises(GradeError):
            obj.grade_value = 0
        with self.assertRaises(GradeError):
            obj.grade_value = '0'
        obj.grade_value = '5'
        with self.assertRaises(GradeError):
            obj.grade_value = StudentError('da')
        with self.assertRaises(GradeError):
            obj.grade_value = 11
        self.assertEqual(obj.__str__(), str(obj.grade_value))


class ServiceTest(unittest.TestCase):
    def test_Service(self):
        obj = Service(StudentService(), DisciplineService(), GradeService())
        self.assertIsNotNone(obj.student_service)
        self.assertIsNotNone(obj.discipline_service)
        self.assertIsNotNone(obj.grade_service)
        self.assertEqual(obj.undo_stack, [])
        self.assertEqual(obj.redo_stack, [])
        self.assertEqual(obj.flag, False)
        obj.initialize_repos()
        self.assertEqual(len(obj.student_service.display()), 10)
        obj.failing()
        self.assertEqual(len(obj.discipline_service.display()), 10)
        obj.best_stats()
        self.assertEqual(len(obj.grade_service.display()), 20)
        obj.discipline_stats()
        with self.assertRaises(IOErr):
            obj.stack_care([])
        obj.flag = True
        obj.stack_care([None])
        self.assertEqual(obj.flag, False)
        obj.undo_stack.clear()
        with self.assertRaises(IOErr):
            obj.undo()
        objet = obj.student_service.store('rollo')
        obj.stack_care([[obj.student_service.store, objet]])
        obj.undo()
        self.assertEqual(len(obj.student_service.display()), 10)
        obj.redo()

        self.assertEqual(len(obj.student_service.display()), 11)
        with self.assertRaises(IOErr):
            obj.redo()
        objet = obj.discipline_service.store('matiee')
        obj.stack_care([[obj.discipline_service.store, objet]])
        self.assertEqual(len(obj.discipline_service.display()), 11)
        obj.undo()
        self.assertEqual(len(obj.discipline_service.display()), 10)
        obj.redo()
        self.assertEqual(len(obj.discipline_service.display()), 11)
        objet = obj.student_service.update('Raul', 'newnaame')
        obj.stack_care([[obj.student_service.update, objet]])
        obj.undo()
        obj.redo()
        objet = obj.discipline_service.update('ASC', 'newdiscipline')
        obj.stack_care([[obj.discipline_service.update, objet]])
        obj.undo()
        obj.redo()
        obj.grade_service.store('discipline_id_test', 'student_id_test', [1, 2, 3])
        obj.stack_care([[obj.grade_service.store, ['discipline_id_test', 'student_id_test', [1, 2, 3]]]])
        obj.undo()
        obj.redo()
        objet = obj.student_service.remove('Andrei')
        obj.stack_care([[obj.student_service.remove, objet]])
        obj.undo()
        obj.redo()
        obj.add_multiple_grades([Grade('id1', 'id2', 1)])
        obj.remove_multiple_grades([Grade('id1', 'id2', 1)])

    def test_StudentService(self):
        obj = StudentService()
        self.assertIsInstance(obj._repo, StudentRepository)
        with self.assertRaises(IOErr):
            obj.store('12sdasdf')
        obj.store('marcus')
        self.assertEqual(obj._repo._list[-1].name, 'marcus')
        with self.assertRaises(IOErr):
            obj.remove('12sdf')
        obj.remove('marcus')
        self.assertEqual(len(obj._repo._list), 0)
        obj.store('marcus')
        self.assertEqual(obj.count_occurence('marcus'), 1)
        obj.update('marcus', 'Joemamma')
        self.assertEqual(obj.count_occurence('Joemamma'), 1)
        self.assertEqual(obj.count_occurence('marcus'), 0)
        self.assertEqual(obj.display(), obj._repo.get_list())
        obj.store('marcus')
        obj.store('marcusA')
        self.assertEqual(len(obj.search('marc')), 2)

    def test_DisciplineService(self):
        obj = DisciplineService()
        self.assertIsInstance(obj._repo, DisciplineRepository)
        with self.assertRaises(IOErr):
            obj.store('12sdf')
        obj.store('Mathabc')
        with self.assertRaises(IOErr):
            obj.remove('12sdfasdf')
        obj.remove('Mathabc')
        self.assertEqual(len(obj.display()), 0)
        obj.store('Math')
        self.assertEqual(obj.count_occurence('Math'), 1)
        obj.update('Math', 'Mathtastic')
        self.assertEqual(obj.count_occurence('Mathtastic'), 1)
        self.assertEqual(obj.count_occurence('Math'), 0)
        self.assertEqual(obj.display(), obj._repo.get_list())
        obj.store('marcus')
        obj.store('marcusA')
        self.assertEqual(len(obj.search('marc')), 2)

    def test_GradeService(self):
        obj = GradeService()
        self.assertIsInstance(obj._repo, GradeRepository)
        obj.store('discipline_id_test', 'student_id_test', [1, 2, 3])
        self.assertEqual(obj.display()[-3].student_id, 'student_id_test')
        self.assertEqual(obj.display()[-3].discipline_id, 'discipline_id_test')
        self.assertEqual(obj.display()[-3].grade_value, 1)
        self.assertEqual(obj.display()[-2].student_id, 'student_id_test')
        self.assertEqual(obj.display()[-2].discipline_id, 'discipline_id_test')
        self.assertEqual(obj.display()[-2].grade_value, 2)
        self.assertEqual(obj.display()[-1].student_id, 'student_id_test')
        self.assertEqual(obj.display()[-1].discipline_id, 'discipline_id_test')
        self.assertEqual(obj.display()[-1].grade_value, 3)
        obj.remove_by_student_id('student_id_test')
        self.assertEqual(len(obj.display()), 0)
        obj.store('discipline_id_test', 'student_id_test', [1, 2, 3])
        obj.remove_by_discipline_id('discipline_id_test')
        self.assertEqual(len(obj.display()), 0)
        obj.store('discipline_id_test', 'student_id_test', [1, 2, 3])
        obj.remove('discipline_id_test', 'student_id_test', 1)
        self.assertEqual(len(obj.display()), 2)


class RepoTest(unittest.TestCase):

    def test_student_repository(self):
        stud_repo = StudentRepository()
        self.assertIsInstance(stud_repo, StudentRepository, 'Wrong instance')
        self.assertIsInstance(stud_repo, Repository, 'Wrong instance')
        self.assertEqual(len(stud_repo._list), 0)
        stud_repo.store(Student('marcel'))
        stud_repo.store(Student('marcelutz'))
        self.assertEqual(stud_repo._list[-1].name, 'marcelutz')
        stud_repo.remove(0)
        self.assertEqual(stud_repo._list[-1].name, 'marcelutz')
        with self.assertRaises(RepoErr):
            stud_repo.remove(20)
        stud_repo.update(-1, 'nomoremarcel')
        self.assertEqual(stud_repo._list[-1].name, 'nomoremarcel')
        with self.assertRaises(RepoErr):
            stud_repo.update(20, 'gaga')
        self.assertEqual(stud_repo.get_list(), stud_repo._list)

    def test_discipline_repository(self):
        disc_repo = DisciplineRepository()
        self.assertIsInstance(disc_repo, DisciplineRepository, 'Wrong instance')
        self.assertIsInstance(disc_repo, Repository, 'Wrong instance')
        self.assertEqual(len(disc_repo._list), 0)
        disc_repo.store(Discipline('Maatee'))
        self.assertEqual(disc_repo._list[-1].name, 'Maatee')
        disc_repo.remove(0)
        disc_repo.store(Discipline('Matha'))
        self.assertEqual(disc_repo._list[-1].name, 'Matha')
        disc_repo.update(-1, 'nomoreMateee')
        self.assertEqual(disc_repo._list[-1].name, 'nomoreMateee')

    def test_grade_repository(self):
        grade_repo = GradeRepository()
        self.assertIsInstance(grade_repo, GradeRepository, 'Wrong instance')
        self.assertIsInstance(grade_repo, Repository, 'Wrong instance')
        self.assertEqual(len(grade_repo._list), 0)
        grade_repo.store(Grade('id1', 'id2', 1))
        self.assertEqual(grade_repo._list[-1].student_id, 'id1')
        self.assertEqual(grade_repo._list[-1].discipline_id, 'id2')
        self.assertEqual(grade_repo._list[-1].grade_value, 1)
        grade_repo.remove(0)
        self.assertEqual(len(grade_repo._list), 0)
        grade_repo.store(Grade('id1', 'id2', 1))
        self.assertEqual(grade_repo._list[0].student_id, 'id1')
        grade_repo.update(-1, 3)
        self.assertEqual(grade_repo._list[-1].grade_value, 3)
