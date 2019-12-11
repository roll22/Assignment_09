from UI.ConsoleUI import UI
from controller.DisciplineController import DisciplineService
from controller.GradeController import GradeService
from controller.MainController import Service
from controller.StudentController import StudentService
from settings.Setup import Setup

setting = 'settings/memory_settings.properties'
setup = Setup(setting)

student_repo = setup.set_student_repo()
discipline_repo = setup.set_discipline_repo()
grade_repo = setup.set_grade_repo()

student_service = StudentService(student_repo)
discipline_service = DisciplineService(discipline_repo)
grade_service = GradeService(grade_repo)
main_service = Service(student_service, discipline_service, grade_service)

if setting == 'settings/memory_settings.properties':
    main_service.initialize_repos()

ui = UI(main_service, student_service, discipline_service, grade_service)
ui.start()
