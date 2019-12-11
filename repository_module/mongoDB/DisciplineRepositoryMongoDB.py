from domain.Discipline import Discipline
from repository_module.mongoDB.RepositoryMongoDB import RepositoryMongoDB


class DisciplineRepositoryMongoDB(RepositoryMongoDB):
    def __init__(self, collection, address):
        super().__init__(collection, address)

    def _load_list(self):
        for obj in self._collection.find():
            self._list.append(Discipline.create_from_data(obj['name'], obj['_id']))
