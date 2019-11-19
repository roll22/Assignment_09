import unittest

from Service import StudentService, DisciplineService, GradeService, IOErr
from repository import Repository, StudentRepository, DisciplineRepository, GradeRepository, RepoErr
from Domain import Student, Discipline, Grade, StudentError, DisciplineError, GradeError


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

    def test_Discipline(self):
        obj = Discipline('Disciplina')
        self.assertEqual(obj.name, 'Disciplina')
        self.assertIsNotNone(obj._id)
        with self.assertRaises(DisciplineError):
            obj.name = 123
        with self.assertRaises(DisciplineError):
            obj.name = '123'
        self.assertEqual(obj.get_id(), obj._id)

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


class ServiceTest(unittest.TestCase):
    def test_StudentService(self):
        obj = StudentService()
        self.assertIsInstance(obj._repo, StudentRepository)
        with self.assertRaises(IOErr):
            obj.add('12sdf')
        obj.add('marcus')
        self.assertEqual(obj._repo._list[-1].name, 'marcus')
        with self.assertRaises(IOErr):
            obj.remove('12sdf')
        obj.remove('marcus')

    def test_DisciplineService(self):
        obj = DisciplineService()
        self.assertIsInstance(obj._repo, DisciplineRepository)
        with self.assertRaises(IOErr):
            obj.add('12sdf')
        obj.add('marcus')
        obj.remove('marcus')


class RepoTest(unittest.TestCase):

    def test_student_repository(self):
        stud_repo = StudentRepository()
        self.assertIsInstance(stud_repo, StudentRepository, 'Wrong instance')
        self.assertIsInstance(stud_repo, Repository, 'Wrong instance')
        self.assertEqual(len(stud_repo._list), 10)
        stud_repo.add(Student('marcel'))
        self.assertEqual(stud_repo._list[-1].name, 'marcel')
        stud_repo.remove(0)
        self.assertEqual(stud_repo._list[0].name, 'Joea')
        with self.assertRaises(RepoErr):
            stud_repo.remove(20)
        stud_repo.update(-1, 'nomoremarcel')
        with self.assertRaises(RepoErr):
            stud_repo.update(20, 'gaga')
        self.assertEqual(stud_repo.get_list(), stud_repo._list)
        self.assertEqual(stud_repo._list[-1].name, 'nomoremarcel')

    def test_discipline_repository(self):
        disc_repo = DisciplineRepository()
        self.assertIsInstance(disc_repo, DisciplineRepository, 'Wrong instance')
        self.assertIsInstance(disc_repo, Repository, 'Wrong instance')
        self.assertEqual(len(disc_repo._list), 10)
        disc_repo.add(Discipline('Maatee'))
        self.assertEqual(disc_repo._list[-1].name, 'Maatee')
        disc_repo.remove(0)
        self.assertEqual(disc_repo._list[0].name, 'Matha')
        disc_repo.update(-1, 'nomoreMateee')
        self.assertEqual(disc_repo._list[-1].name, 'nomoreMateee')

    def test_grade_repository(self):
        grade_repo = GradeRepository()
        self.assertIsInstance(grade_repo, GradeRepository, 'Wrong instance')
        self.assertIsInstance(grade_repo, Repository, 'Wrong instance')
        self.assertEqual(len(grade_repo._list), 10)
        grade_repo.add(Grade('id1', 'id2', 1))
        self.assertEqual(grade_repo._list[-1].student_id, 'id1')
        self.assertEqual(grade_repo._list[-1].discipline_id, 'id2')
        self.assertEqual(grade_repo._list[-1].grade_value, 1)
        grade_repo.remove(0)
        self.assertEqual(grade_repo._list[0].student_id, 'joe1_id')
        grade_repo.update(-1, 3)
        self.assertEqual(grade_repo._list[-1].grade_value, 3)
