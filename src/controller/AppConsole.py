from ..utils.CsvHelper import CsvHelper
from ..view.View import View
from ..model.Student import Student
from ..model.Subject import Subject


class AppConsole:

    @classmethod
    def mainLoop(cls):
        csvHelper = CsvHelper("resources/students.csv", "resources/subjects.csv", "resources/registrations.csv")
        mainLoop = True

        while mainLoop:
            students, subjects, registrations = csvHelper.loadAll()
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
                    if not idExists:
                        student = Student(id,
                                          View.askString("Insert the student name: "),
                                          View.askInt("Insert the student age: "),
                                          View.askString("Insert the student gender: "))
                        csvHelper.addStudent(student)

                case 2:
                    idExists = False
                    id = View.askString("Insert the subject ID: ")
                    for subject in subjects:
                        if subject['id'] == id:
                            View.printError("The subject ID is already in use.")
                            idExists = True
                            break
                    if not idExists:
                        subject = Subject(id, View.askString("Insert the subject name: "))
                        csvHelper.addSubject(subject)

                case 3:
                    studentId = View.askString("Insert the student ID: ")
                    subjectId = View.askString("Insert the subject ID: ")
                    studentFound = False
                    subjectFound = False
                    for s in students:
                        if s['id'] == studentId:
                            studentFound = True
                            break
                    for sub in subjects:
                        if sub['id'] == subjectId:
                            subjectFound = True
                            break
                    if not studentFound:
                        View.printError("Student ID not found.")
                    elif not subjectFound:
                        View.printError("Subject ID not found.")
                    else:
                        csvHelper.enrollStudent(Subject(subjectId, ""), Student(studentId, "", 0, ""))

                case 4:
                    View.printStudents(students)

                case 5:
                    View.printSubjects(subjects)

                case 6:
                    studentId = View.askString("Insert the student ID to edit: ")
                    studentFound = False
                    for student in students:
                        if student['id'] == studentId:
                            studentFound = True
                            newName = View.askString("Insert the new name: ")
                            newAge = View.askInt("Insert the new age: ")
                            newGender = View.askString("Insert the new gender: ")
                            csvHelper.editStudent(students, studentId, newName, newAge, newGender)
                            break
                    if not studentFound:
                        View.printError("Student ID not found.")

                case 7:
                    subjectId = View.askString("Insert the subject ID to edit: ")
                    subjectFound = False
                    for subject in subjects:
                        if subject['id'] == subjectId:
                            subjectFound = True
                            newName = View.askString("Insert the new name: ")
                            csvHelper.editSubject(subjects, subjectId, newName)
                            break
                    if not subjectFound:
                        View.printError("Subject ID not found.")

                case 8:
                    studentId = View.askString("Insert the student ID to delete: ")
                    studentFound = False
                    for student in students:
                        if student['id'] == studentId:
                            studentFound = True
                            csvHelper.deleteStudent(students, registrations, studentId)
                            break
                    if not studentFound:
                        View.printError("Student ID not found.")

                case 9:
                    subjectId = View.askString("Insert the subject ID to delete: ")
                    subjectFound = False
                    for subject in subjects:
                        if subject['id'] == subjectId:
                            subjectFound = True
                            csvHelper.deleteSubject(subjects, registrations, subjectId)
                            break
                    if not subjectFound:
                        View.printError("Subject ID not found.")

                case 10:
                    subjectId = View.askString("Insert the subject ID: ")
                    studentId = View.askString("Insert the student ID: ")
                    enrollmentFound = False
                    for r in registrations:
                        if r["studentId"] == studentId and r["subjectId"] == subjectId:
                            enrollmentFound = True
                            csvHelper.deleteEnrollment(subjectId, studentId)
                            break
                    if not enrollmentFound:
                        View.printError("Enrollment not found.")

                case 0:
                    mainLoop = False
                case _:
                    View.printError("Invalid option.")
