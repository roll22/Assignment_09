from repository_module.RepoErr import RepoErr


class Repository:
    def __init__(self):
        self._list = []

    def store(self, obj):
        """
        Adds an object to the list
        :param obj:
        """
        self._list.append(obj)

    def remove(self, index):
        """
        Removes an object from the list
        :raises RepoErr if doesn't find the object
        :param index:
        """
        try:
            return self._list.pop(index)
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
            obj = self._list[index]
            self._list[index].name = value
            return obj
        except Exception:
            raise RepoErr("Object not found!")

    def get_list(self):
        return self._list
