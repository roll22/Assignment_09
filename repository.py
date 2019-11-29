from Domain import *


class RepoErr(Exception):
    pass


class Repository:
    def __init__(self):
        self._list = []

    def add(self, object):
        """
        Adds an object to the list
        :param object:
        """
        self._list.append(object)

    def remove(self, index):
        """
        Removes an object from the list
        :raises RepoErr if doesn't find the object
        :param index:
        """
        try:
            self._list.pop(index)
        except Exception:
            raise RepoErr("Object Not Found!")

    def update(self, index, value):
        """
        Updates the object's property at specified index with the given value
        Overridable for different properties
        :raises RepoErr if doesn't find the object
        :param index:
        :param value:
        """
        try:
            self._list[index].name = value
        except Exception:
            raise RepoErr("Object not found!")

    def get_list(self):
        return self._list


class StudentRepository(Repository):
    def __init__(self):
        super().__init__()


class DisciplineRepository(Repository):
    def __init__(self):
        super().__init__()


class GradeRepository(Repository):
    def __init__(self):
        super().__init__()

    def update(self, index, value):
        self._list[index].grade_value = value


"""
# print(myclient.list_database_names())


# import pymongo
#
#
# class Repository:
#     def __init__(self):
#         self._myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#         dblist = self._myclient.list_database_names()
#         if "students" in dblist:
#             raise RepoErr('Students not found!')
#
#
# mydb = myclient["mydatabase"]
#
# print(mydb)
# mycol = mydb["customers"]
#
# mydict = {"value": "John", "address": "Highway 37"}
#
# x = mycol.insert_one(mydict)
#
# print(x.inserted_id, ' calkutxc')
"""

"""
check if database exists
    yes
        tell user
        set as my database
    no
        tell user
        create_database
        confirm success
        set as my database
        
check if collections exist
    yes
        tell user
        set as own collections
    no
        tell user
        create new collections
        set as own collections

Collections:        
    students
    disciplines
    grades
    
    
implement insert_one()


"""
