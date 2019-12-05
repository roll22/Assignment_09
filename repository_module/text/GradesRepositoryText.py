from domain.Grade import Grade
from repository_module.memory.GradeRepository import GradeRepository


class GradeRepositoryText(GradeRepository):
    def __init__(self, path):
        super().__init__()
        self._path = path
        self._load_file()

    def _load_file(self):
        file = open(self._path, 'r')
        line = file.readline()
        while line:
            line = line.strip().split()
            stud_id = line[0]
            disc_id = line[1]
            value = line[2]
            obj = Grade(discipline_id=disc_id, student_id=stud_id, grade_value=value)
            self._list.append(obj)
            line = file.readline()
        file.close()

    def store(self, object):
        super().store(object)
        self._save_file()

    def remove(self, index):
        ret = super().remove(index)
        self._save_file()
        return ret

    def update(self, index, value):
        ret = super().update(index, value)
        self._save_file()
        return ret

    def _save_file(self):
        file = open(self._path, 'w')

        for obj in self._list:
            line = str(obj.student_id) + ' ' + str(obj.discipline_id) + ' ' + str(obj.grade_value) + '\n'
            file.write(line)

        file.close()
