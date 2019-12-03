from UI.ConsoleUI import UI
from controller.DisciplineController import DisciplineService
from controller.GradeController import GradeService
from controller.StudentController import StudentService

student_service = StudentService()
discipline_service = DisciplineService()
grade_service = GradeService()
ui = UI(student_service, discipline_service, grade_service)
ui.start()
