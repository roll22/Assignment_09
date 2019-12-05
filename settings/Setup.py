import javaproperties

from repository_module.json.DisciplineRepositoryJSON import DisciplineRepositoryJSON
from repository_module.json.GradeRepositoryJSON import GradeRepositoryJSON
from repository_module.json.StudentRepositoryJSON import StudentRepositoryJSON
from repository_module.binary.DisciplineRepositoryBinary import DisciplineRepositoryBinary
from repository_module.binary.GradeRepositoryBinary import GradeRepositoryBinary
from repository_module.binary.StudentRepositoryBinary import StudentRepositoryBinary
from repository_module.text.DisciplineRepositoryText import DisciplineRepositoryText
from repository_module.text.GradesRepositoryText import GradeRepositoryText
from repository_module.text.StudentRepositoryText import StudentRepositoryText
from repository_module.memory.DisciplineRepository import DisciplineRepository
from repository_module.memory.GradeRepository import GradeRepository
from repository_module.memory.StudentRepository import StudentRepository


class Setup:
    def __init__(self, setting):
        self._setting = setting
        self._settings = self._load_settings()
        self.repo_map = {
            'StudentRepositoryText': StudentRepositoryText,
            'DisciplineRepositoryText': DisciplineRepositoryText,
            'GradeRepositoryText': GradeRepositoryText,
            'StudentRepositoryBinary': StudentRepositoryBinary,
            'DisciplineRepositoryBinary': DisciplineRepositoryBinary,
            'GradeRepositoryBinary': GradeRepositoryBinary,
            'StudentRepositoryJSON': StudentRepositoryJSON,
            'DisciplineRepositoryJSON': DisciplineRepositoryJSON,
            'GradeRepositoryJSON': GradeRepositoryJSON,
            'StudentRepository': StudentRepository,
            'DisciplineRepository': DisciplineRepository,
            'GradeRepository': GradeRepository,
        }

    def _load_settings(self):
        with open(self._setting, 'r', encoding='latin-1') as fp:
            return javaproperties.load(fp)

    def set_student_repo(self):
        if self._settings['student_repo'] == 'StudentRepository':
            return self.repo_map[self._settings['student_repo']]()
        else:
            return self.repo_map[self._settings['student_repo']](self._settings['stud_path'])

    def set_discipline_repo(self):
        if self._settings['discipline_repo'] == 'DisciplineRepository':
            return self.repo_map[self._settings['discipline_repo']]()
        else:
            return self.repo_map[self._settings['discipline_repo']](self._settings['disc_path'])

    def set_grade_repo(self):
        if self._settings['grade_repo'] == 'GradeRepository':
            return self.repo_map[self._settings['grade_repo']]()
        else:
            return self.repo_map[self._settings['grade_repo']](self._settings['grade_path'])
