import json

from domain.Grade import Grade
from repository_module.memory.GradeRepository import GradeRepository


class GradeRepositoryJSON(GradeRepository):
    def __init__(self, path):
        super().__init__()
        self._path = path
        try:
            self._load_file()
        except Exception:
            pass

    def _load_file(self):
        with open(self._path, 'r') as fp:
            data = json.load(fp)
            for obj in data['grades']:
                stud_id = obj['student_id']
                disc_id = obj['discipline_id']
                value = obj['grade_value']
                obj = Grade(discipline_id=disc_id, student_id=stud_id, grade_value=value)
                self._list.append(obj)
        fp.close()

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
        with open(self._path, 'w') as outfile:
            main = {'grades': []}
            for obj in self._list:
                main['grades'].append(obj.to_dict())
            json.dump(main, outfile)
            outfile.close()
