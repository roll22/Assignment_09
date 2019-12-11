import pymongo

from repository_module.memory.Repository import Repository


class RepositoryMongoDB(Repository):
    def __init__(self, collection, address="mongodb://localhost:27017/"):
        super().__init__()
        self._client = pymongo.MongoClient(address)
        self._db = self._client["mydatabase"]
        self._collection = self._db[collection]
        self._load_list() 

    def _load_list(self):
        pass

    def store(self, obj):
        super().store(obj)
        self._collection.insert_one(obj.to_dict())

    def remove(self, index):
        obj = super().remove(index)
        query = {"_id": obj.get_id()}
        self._collection.delete_one(query)
        return obj

    def update(self, index, value):
        obj = super().update(index, value)
        query = {"_id": obj.get_id()}
        new_value = {"$set": {"name": value}}
        self._collection.update_one(query, new_value)
        return obj

    def get_list(self):
        return super().get_list()
