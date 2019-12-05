import pickle

from repository_module.memory.StudentRepository import StudentRepository


class StudentRepositoryBinary(StudentRepository):
    def __init__(self, path):
        super().__init__()
        self._path = path
        self._load_file()

    def _load_file(self):
        file = open(self._path, "rb")
        self._list = pickle.load(file)
        file.close()

    def _save_file(self):
        file = open(self._path, "wb")
        pickle.dump(self._list, file)
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
