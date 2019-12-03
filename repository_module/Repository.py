from repository_module.RepoErr import RepoErr


class Repository:
    def __init__(self):
        self._list = []

    def store(self, object):
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