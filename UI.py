from Service import Service
from sys import exit
from Domain import Student, Discipline, Grade


class IOErr(Exception):
    pass


class UI:
    def __init__(self, svc):
        self._service = svc

    @property
    def service(self):
        return self._service

    @staticmethod
    def print_main():
        print("\n"
              "1.add\n"
              "2.remove\n"
              "3.update\n"
              "4.list")

    @staticmethod
    def read_choice():
        """
        Reads input choice
        :return: int choice
        """
        raw_input = input('>')
        if not raw_input.isdigit():
            raise IOErr('Bad Choice!')
        raw_input = int(raw_input)
        if not 1 <= raw_input <= 4:  # TODO keep track of the number of available functions
            raise IOErr('Bad Choice!')
        return raw_input

    def return_cmd(self, choice):
        commands = {
            '1': self.add_menu,
            '2': self.remove_menu,
            '3': self.update_menu,
            '4': self.list,
            '5': exit
        }
        return commands[choice]

    def start(self):
        while True:
            self.actual_start()

    def actual_start(self):
        self.print_main()
        choice = self.read_choice()
        cmd = self.return_cmd(choice)
        cmd()


service = Service()
ui = UI(service)
ui.start()
