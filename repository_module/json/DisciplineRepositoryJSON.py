import json

from domain.Discipline import Discipline
from repository_module.memory.DisciplineRepository import DisciplineRepository


class DisciplineRepositoryJSON(DisciplineRepository):
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
            for obj in data['disciplines']:
                id = obj['_id']
                name = obj['name']
                obj = Discipline.create_from_data(name, id)
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
            main = {'disciplines': []}
            for obj in self._list:
                main['disciplines'].append(obj.to_dict())
            json.dump(main, outfile)
            outfile.close()
