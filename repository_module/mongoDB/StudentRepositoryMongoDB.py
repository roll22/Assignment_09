from domain.Student import Student
from repository_module.mongoDB.RepositoryMongoDB import RepositoryMongoDB


class StudentRepositoryMongoDB(RepositoryMongoDB):
    def __init__(self, collection, address):
        super().__init__(collection, address)

    def _load_list(self):
        for obj in self._collection.find():
            self._list.append(Student.create_from_data(obj['name'], obj['_id']))
