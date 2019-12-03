import re

from domain.Discipline import Discipline
from repository_module.DisciplineRepository import DisciplineRepository
from controller.IOErr import IOErr


class DisciplineService:
    def __init__(self):
        self._repo = DisciplineRepository()

    def add_obj(self, obj):
        self._repo.store(obj)

    def store(self, name):
        """
        Makes validations, creates the object and calls the repo Add
        :raises: IOErr
        """
        if not name.isalpha():
            raise IOErr("name must be literal")
        obj = Discipline(name)
        self._repo.store(obj)
        return obj

    def remove(self, name):
        """
        Makes validations, finds the index and calls the repo remove
        Calls the GradeServices repo remove
        :raises: IOErr
        """
        if not name.isalpha():
            raise IOErr("name must be literal")
        _list = self._repo.get_list()
        for idx, discipline in enumerate(_list):
            if discipline.name == name:
                disc_id = discipline.get_id()
                self._repo.remove(index=idx)
                return discipline

    def count_occurence(self, name):
        """
        Counts the occurences of a name in the list
        :param name:
        :return: count<int>
        """
        _list = self._repo.get_list()
        count = 0
        for idx, discipline in enumerate(_list):
            if discipline.name == name:
                count += 1
        return count

    def update(self, name, new_name):
        """
        Updates the name of the discipline with a new name
        :param name:
        :param new_name:
        :return:
        """
        _list = self._repo.get_list()
        for idx, discipline in enumerate(_list):
            if discipline.name == name:
                discipline.name = new_name
                break
        return name, new_name

    def display(self):
        return self._repo.get_list()

    def search(self, match):
        match = '^' + match
        returns = []
        _list = self._repo.get_list()
        for idx, discipline in enumerate(_list):
            if re.search(match, discipline.name, re.IGNORECASE) is not None:
                returns.append([discipline.name, discipline.get_id()])
        return returns
