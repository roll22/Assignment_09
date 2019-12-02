import unittest

from Service import StudentService, DisciplineService, GradeService, IOErr, Service
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
        obj.initialize_repos()
        self.assertEqual(len(obj.student_service.display()), 10)
        obj.failing()
        self.assertEqual(len(obj.discipline_service.display()), 10)
        obj.best_stats()
        self.assertEqual(len(obj.grade_service.display()), 20)
        obj.discipline_stats()


    def test_StudentService(self):
        obj = StudentService()
        self.assertIsInstance(obj._repo, StudentRepository)
        with self.assertRaises(IOErr):
            obj.add('12sdasdf')
        obj.add('marcus')
        self.assertEqual(obj._repo._list[-1].name, 'marcus')
        with self.assertRaises(IOErr):
            obj.remove('12sdf')
        obj.remove('marcus')
        self.assertEqual(len(obj._repo._list), 0)
        obj.add('marcus')
        self.assertEqual(obj.count_occurence('marcus'), 1)
        obj.update('marcus', 'Joemamma')
        self.assertEqual(obj.count_occurence('Joemamma'), 1)
        self.assertEqual(obj.count_occurence('marcus'), 0)
        self.assertEqual(obj.display(), obj._repo.get_list())
        obj.add('marcus')
        obj.add('marcusA')
        self.assertEqual(len(obj.search('marc')), 2)

    def test_DisciplineService(self):
        obj = DisciplineService()
        self.assertIsInstance(obj._repo, DisciplineRepository)
        with self.assertRaises(IOErr):
            obj.add('12sdf')
        obj.add('Mathabc')
        with self.assertRaises(IOErr):
            obj.remove('12sdfasdf')
        obj.remove('Mathabc')
        self.assertEqual(len(obj.display()), 0)
        obj.add('Math')
        self.assertEqual(obj.count_occurence('Math'), 1)
        obj.update('Math', 'Mathtastic')
        self.assertEqual(obj.count_occurence('Mathtastic'), 1)
        self.assertEqual(obj.count_occurence('Math'), 0)
        self.assertEqual(obj.display(), obj._repo.get_list())
        obj.add('marcus')
        obj.add('marcusA')
        self.assertEqual(len(obj.search('marc')), 2)

    def test_GradeService(self):
        obj = GradeService()
        self.assertIsInstance(obj._repo, GradeRepository)
        obj.add('discipline_id_test', 'student_id_test', [1, 2, 3])
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
        obj.add('discipline_id_test', 'student_id_test', [1, 2, 3])
        obj.remove_by_discipline_id('student_id_test')
        self.assertEqual(len(obj.display()), 0)


class RepoTest(unittest.TestCase):

    def test_student_repository(self):
        stud_repo = StudentRepository()
        self.assertIsInstance(stud_repo, StudentRepository, 'Wrong instance')
        self.assertIsInstance(stud_repo, Repository, 'Wrong instance')
        self.assertEqual(len(stud_repo._list), 0)
        stud_repo.add(Student('marcel'))
        stud_repo.add(Student('marcelutz'))
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
        disc_repo.add(Discipline('Maatee'))
        self.assertEqual(disc_repo._list[-1].name, 'Maatee')
        disc_repo.remove(0)
        disc_repo.add(Discipline('Matha'))
        self.assertEqual(disc_repo._list[-1].name, 'Matha')
        disc_repo.update(-1, 'nomoreMateee')
        self.assertEqual(disc_repo._list[-1].name, 'nomoreMateee')

    def test_grade_repository(self):
        grade_repo = GradeRepository()
        self.assertIsInstance(grade_repo, GradeRepository, 'Wrong instance')
        self.assertIsInstance(grade_repo, Repository, 'Wrong instance')
        self.assertEqual(len(grade_repo._list), 0)
        grade_repo.add(Grade('id1', 'id2', 1))
        self.assertEqual(grade_repo._list[-1].student_id, 'id1')
        self.assertEqual(grade_repo._list[-1].discipline_id, 'id2')
        self.assertEqual(grade_repo._list[-1].grade_value, 1)
        grade_repo.remove(0)
        self.assertEqual(len(grade_repo._list), 0)
        grade_repo.add(Grade('id1', 'id2', 1))
        self.assertEqual(grade_repo._list[0].student_id, 'id1')
        grade_repo.update(-1, 3)
        self.assertEqual(grade_repo._list[-1].grade_value, 3)
