class ServiceErr(Exception):
    pass


class StudentError(ServiceErr):
    def __init__(self, string):
        pass


class DisciplineError(ServiceErr):
    def __init__(self, string):
        pass


class GradeError(ServiceErr):
    def __init__(self, string):
        pass