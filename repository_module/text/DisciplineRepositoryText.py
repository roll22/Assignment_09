from domain.Discipline import Discipline
from repository_module.memory.DisciplineRepository import DisciplineRepository


class DisciplineRepositoryText(DisciplineRepository):
    def __init__(self, path):
        super().__init__()
        self._path = path
        self._load_file()

    def _load_file(self):
        file = open(self._path, 'r')
        line = file.readline()
        while line:
            line = line.strip().split()
            name = line[0]
            id = line[1]
            obj = Discipline.create_from_data(name, id)
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
            line = str(obj.name) + ' ' + str(obj.get_id()) + '\n'
            file.write(line)

        file.close()
