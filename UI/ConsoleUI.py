from sys import exit

from UI.IOErr import IOErr
from controller.MainController import Service


class UI:
    def __init__(self, main_svc, stud_svc, disc_svc, grade_svc):
        self._stud = stud_svc
        self._disc = disc_svc
        self._grad = grade_svc
        self._service = main_svc

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

    @staticmethod
    def print_list(_list):
        for obj in _list:
            print(obj.name, obj.get_id())

    def add_menu(self):
        print('1.Add Student')
        print('2.Add Discipline')
        choice = input('>')
        if choice == '1':
            name = input('input name>')
            obj = self.student_service.add(name=name)
            self.service.stack_care([[self.student_service.add, obj]])
        elif choice == '2':
            name = input('input discipline>')
            obj = self.discipline_service.add(name=name)
            self.service.stack_care([[self.discipline_service.add, obj]])
        else:
            raise IOErr('Bad choice!')

    def remove_menu(self):
        print('1.Remove Student')
        print('2.Remove Discipline')
        choice = input('>')
        if choice == '1':
            name = input('Name>')
            obj = self.student_service.remove(name=name)
            _list_of_deleted_grades = self.grade_service.remove_by_student_id(obj.get_id())
            self.service.stack_care(
                [[self.student_service.remove, obj], [self.grade_service.remove_by_student_id, _list_of_deleted_grades]]
            )
        elif choice == '2':
            discipline = input('Discipline>')
            obj = self.discipline_service.remove(name=discipline)
            _list_of_deleted_grades = self.grade_service.remove_by_discipline_id(obj.get_id())
            self.service.stack_care(
                [[self.discipline_service.remove, obj],
                 [self.grade_service.remove_by_discipline_id, _list_of_deleted_grades]]
            )
        else:
            raise IOErr('Bad choice!')

    def update_menu(self):
        print('1.Update Student')
        print('2.Update Discipline')
        choice = input('>')
        if choice == '1':
            name = input('Name>')
            if self.student_service.count_occurence(name=name) > 0:
                new_name = input('Input new value >')
                obj = list(self.student_service.update(name, new_name))
                self.service.stack_care([[self.student_service.update, obj]])
            else:
                raise IOErr("Student not found")
        elif choice == '2':
            name = input('Discipline >')
            if self.discipline_service.count_occurence(name=name) > 0:
                new_name = input('Input new value >')
                obj = list(self.discipline_service.update(name, new_name))
                self.service.stack_care([[self.discipline_service.update, obj]])
            else:
                raise IOErr("Discipline not found")
        else:
            raise IOErr('Bad choice!')

    def display(self):
        print('1.Display by Students')
        print('2.Display by Disciplines')
        print('3.Display by Grades')
        choice = input('>')
        if choice == '1':
            _list = self.student_service.display()
            self.print_list(_list)
        elif choice == '2':
            _list = self.discipline_service.display()
            self.print_list(_list)
        elif choice == '3':
            _list = self.grade_service.display()
            self.print_grades(_list)
        else:
            raise IOErr('Bad choice!')

    def grade_menu(self):
        discipline = input('Discipline>')
        if not self.discipline_service.count_occurence(discipline) > 0:
            raise IOErr('Discipline not Found!')
        disc_id = None
        for _discipline in self.discipline_service.display():
            if _discipline.name == discipline:
                disc_id = _discipline.get_id()
                break
        name = input('Name>')
        if not self.student_service.count_occurence(name) > 0:
            raise IOErr('Student not Found!')
        student_id = None
        for student in self.student_service.display():
            if student.name == name:
                student_id = student.get_id()
                break
        grades = input('Grades>')
        grades = grades.split()
        try:
            final_grades = list(int(value) for value in grades)
        except Exception:
            raise IOErr('Bad Grades!')
        self.grade_service.add(disc_id, student_id, final_grades)
        self.service.stack_care([[self.grade_service.add, [disc_id, student_id, final_grades]]])

    def search_menu(self):
        print('1.Search Students')
        print('2.Search Disciplines')
        choice = input('>')
        if choice == '1':
            search = input('>')
            self.print_search(self.student_service.search(search))
        elif choice == '2':
            search = input('>')
            self.print_search(self.discipline_service.search(search))
        else:
            raise IOErr('Bad Choice.')

    @staticmethod
    def print_search(printable_list):
        for item in printable_list:
            print(item[0], item[1])

    @staticmethod
    def print_stats(_list):
        for elem in _list:
            printable = ''
            for small_elem in elem:
                printable += str(small_elem)
                printable += ' '
            print(printable)

    @staticmethod
    def print_grades(_list):
        for x in _list:
            print("stud_id: " + str(x.student_id) +
                  " disc_id: " + str(x.discipline_id) +
                  " grade: " + str(x.grade_value))

    def statistics_menu(self):
        print('1.Failing')
        print('2.Best Grades')
        print('3.Discipline Stats')
        choice = input('>')
        if choice == '1':
            _list = self.service.failing()
            self.print_stats(_list)
        elif choice == '2':
            _list = self.service.best_stats()
            self.print_stats(_list)
        elif choice == '3':
            _list = self.service.discipline_stats()
            self.print_stats(_list)
        else:
            raise IOErr('Bad Choice.')

    def undo(self):
        self.service.undo()

    def redo(self):
        self.service.redo()

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
        if choice in [
            '1',
            '2',
            '3',
            '5',
            '1',

        ]:
            pass
