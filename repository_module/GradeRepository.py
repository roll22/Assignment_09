from repository_module.Repository import Repository


class GradeRepository(Repository):
    def __init__(self):
        super().__init__()

    def update(self, index, value):
        self._list[index].grade_value = value
