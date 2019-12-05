import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mydict = {"name": "John", "address": "Highway 37"}

x = mycol.insert_one(mydict)

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
