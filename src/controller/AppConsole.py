from ..utils.CsvHelper import CsvHelper
from ..view.View import View
from ..model.Student import Student
from ..model.Subject import Subject

class AppConsole:

    @classmethod
    def mainLoop(cls):
        csvHelper = CsvHelper("resources/students.csv","resources/subjects.csv")
        mainLoop = True

        while mainLoop:
            students = csvHelper.loadStudents()
            subjects = csvHelper.loadSubjects()

            option = View.mainMenu()

            match option:
                case 1:
                    idExists = False
                    id = View.askString("Insert the student ID: ")
                    for student in students:
                        if student['id'] == id:
                            View.printError("The student ID is already in use.")
                            idExists = True
                            break

                    if idExists == False:
                        student = Student(id,
                                          View.askString("Insert the student name: "),
                                          View.askInt("Insert the student age: "),
                                          View.askString("Insert the student gender: "))

                        csvHelper.addStudent(student)

                case 2:
                    nameExists = False
                    subjectName = View.askString("Insert the subject name: ")
                    for subject in subjects:
                        if subjectName == subject['name']:
                            View.printError("The subject name is already in use.")
                            nameExists = True
                            break

                    if nameExists == False:
                        subject = Subject(subjectName)
                        csvHelper.addSubject(subject)

                case 3:
                    id = View.askString("Insert the student ID: ")
                    subjectName = View.askString("Insert the subject name: ")
                    csvHelper.enrollStudent(subjectName, id, subjects, students)

                case 4:
                    View.printStudents(students)

                case 5:
                    View.printSubject(subjects, students)

                case 0:
                    mainLoop = False
                case _:
                    View.printError("Invalid option.")


