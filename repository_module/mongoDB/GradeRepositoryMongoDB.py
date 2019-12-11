import pymongo

from domain.Grade import Grade
from repository_module.memory.GradeRepository import GradeRepository


class GradeRepositoryMongoDB(GradeRepository):
    def __init__(self, collection, address):
        super().__init__()
        self._client = pymongo.MongoClient(address)
        self._db = self._client["mydatabase"]
        self._collection = self._db[collection]
        self._load_list()

    def _load_list(self):
        for obj in self._collection.find():
            self._list.append(Grade(obj['student_id'], obj['discipline_id'], obj['grade_value']))

    def store(self, obj):
        super().store(obj)
        self._collection.insert_one(obj.to_dict())

    def remove(self, index):
        obj = super().remove(index)
        query = {"discipline_id": obj.discipline_id, "student_id": obj.student_id, "grade_value": obj.grade_value}
        self._collection.delete_one(query)
        return obj

    def update(self, index, value):
        obj = super().update(index, value)
        query = {"discipline_id": obj.discipline_id, "student_id": obj.student_id, "grade_value": obj.grade_value}
        new_value = {"$set": {"grade_value": value}}
        self._collection.update_one(query, new_value)
        return obj

    def get_list(self):
        return super().get_list()
