from repository_module.memory.Repository import Repository


class GradeRepository(Repository):
    def __init__(self):
        super().__init__()

    def update(self, index, value):
        obj =self._list[index]
        self._list[index].grade_value = value
        return obj
