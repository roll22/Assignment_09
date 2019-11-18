from Service import Service, StudentService, DisciplineService, GradeService
from sys import exit
from Domain import Student, Discipline, Grade


class IOErr(Exception):
    pass


class UI:
    def __init__(self, svc, stud_svc, disc_svc, grade_svc):
        self._service = svc
        self._stud = stud_svc
        self._disc = disc_svc
        self._grad = grade_svc

    @property
    def service(self):
        return self._service

    @property
    def student_service(self):
        return self._stud

    @property
    def discipline_service(self):
        return self._disc

    @property
    def grade_service(self):
        return self._grad

    @staticmethod
    def print_main():
        print("\n"
              "0.exit\n"
              "1.add\n"
              "2.remove\n"
              "3.update\n"
              "4.list\n"
              "5.grade\n"
              "6.search\n"
              "7.statistics\n"
              "8.undo\n"
              "9.redo\n")

    @staticmethod
    def read_choice():
        """
        Reads input choice
        :return: int choice
        """
        raw_input = input('>')
        if not raw_input.isdigit():
            raise IOErr('Bad Choice!')
        raw_int = int(raw_input)
        if not 0 <= raw_int <= 9:
            raise IOErr('Bad Choice!')
        return raw_input

    def add_menu(self):
        print('1.Add Student')
        print('2.Add Discipline')
        choice = input('>')
        if choice == '1':
            name = input('input value > ')
            # TODO call service function
        elif choice == '2':
            name = input('input discipline > ')
            # TODO call service function
        else:
            raise IOErr('Bad choice!')

    def remove_menu(self):
        print('1.Remove Student')
        print('2.Remove Discipline')
        choice = input('>')
        if choice == '1':
            name = input('Name>')
            # TODO call service STUDENT remove by Name
        elif choice == '2':
            discipline = input('Discipline>')
            # TODO call service DISCIPLINE remove by Name
        else:
            raise IOErr('Bad choice!')

    def update_menu(self):
        print('1.Update Student')
        print('2.Update Discipline')
        choice = input('>')
        if choice == '1':
            name = input('Name>')
            # TODO call service STUDENT Check by Name return no of results
            # if > 0
            # new_name = input('Input new value >')
            # TODO call service STUDENT Update by Name
        elif choice == '2':
            name = input('Discipline >')
            # TODO call service DISCIPLINE Check by Name return no of results
            # if > 0
            # new_name = input('Input new value >')
            # TODO call service DISCIPLINE Update by Name
        else:
            raise IOErr('Bad choice!')

    def display(self):
        print('1.Display by Students')
        print('2.Display by Disciplines')
        choice = input('>')
        if choice == '1':
            # TODO call service STUDENTS DISPLAY
            pass
        elif choice == '2':
            # TODO call service DISCIPLINES DISPLAY
            pass
        else:
            raise IOErr('Bad choice!')

    def grade_menu(self):
        discipline = input('Discipline>')
        # TODO check DISCIPLINE
        # if == 1
        # else raise
        name = input('Name>')
        # TODO check STUDENT
        # if == 1
        # else raise
        grades = input('Grades>')
        grades = grades.split()
        for idx, grade in enumerate(grades):
            try:
                grades[idx] = int(grade)
            except Exception:
                raise IOErr('Bad Grades!')
        # TODO call service GRADE at discipline, value: grades

    def search_menu(self):
        print('1.Search Students')
        print('2.Search Disciplines')
        choice = input('>')
        if choice == '1':
            search = input('>')
            # TODO call service search
        elif choice == '2':
            search = input('>')
            # TODO call service search
        else:
            raise IOErr('Bad Choice.')

    def statistics_menu(self):
        print('1.Failing')
        print('2.Best Grades')
        choice = input('>')
        if choice == '1':
            search = input('>')
            # TODO call service search
        elif choice == '2':
            search = input('>')
            # TODO call service search
        else:
            raise IOErr('Bad Choice.')

    def undo(self):
        pass

    def redo(self):
        pass

    def return_cmd(self, choice):
        commands = {
            '1': self.add_menu,
            '2': self.remove_menu,
            '3': self.update_menu,
            '4': self.display,
            '5': self.grade_menu,
            '6': self.search_menu,
            '7': self.statistics_menu,
            '8': self.undo,
            '9': self.redo,
            '0': exit,
        }
        return commands[choice]

    def start(self):
        while True:
            try:
                self.actual_start()
            except Exception as err:
                print(err.args[0])

    def actual_start(self):
        self.print_main()
        choice = self.read_choice()
        self.return_cmd(choice)()


general_service = Service()
student_service = StudentService()
discipline_service = DisciplineService()
grade_service = GradeService()
ui = UI(general_service, student_service, discipline_service, grade_service)
ui.start()
