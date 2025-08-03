from ..model.Student import Student
from ..model.Subject import Subject
from ..view.View import View


class CsvHelper:
    def __init__(self, studentFilepath : str, subjectFilepath : str):
        self.studentFilepath = studentFilepath
        self.subjectFilepath = subjectFilepath

    def loadStudents(self):

        students = []

        with open(self.studentFilepath, 'r') as f:
            i = 0
            for line in f.readlines():
                student = line.strip().split(',')
                if i > 0:
                    students.append({
                        "id" : str(student[0]),
                        "name" : str(student[1]),
                        "age" : int(student[2]),
                        "gender" : str(student[3])
                    })
                i += 1

            return students

    def loadSubjects(self):

        subjects = []

        with open(self.subjectFilepath, 'r') as f:
            i = 0
            for line in f.readlines():
                subject = line.strip().split(',')
                if i > 0:
                    subjects.append({
                        "name" : str(subject[0]),
                        "students" : [] if subject[1] is None else [str(student) for student in subject[1].split('-')]
                    })
                i += 1

            return subjects

    def addStudent(self, student: Student):
        studentString = '\n' + str(student.getId()) + "," + str(student.getName()) + "," + str(student.getAge()) + "," + str(student.getGender())

        with open(self.studentFilepath, 'a') as f:
            f.writelines([studentString])

    def addSubject(self, subject: Subject):
        subjectString = '\n' + str(subject.getName()) + "," + "-".join([student.getId() for student in subject.getStudents()])

        with open(self.subjectFilepath, 'a') as f:
            f.write(subjectString)

    def enrollStudent(self, subjectName: str, studentId: str, subjects: list, students: list):
        for subject in subjects:
            if subjectName == subject['name']:
                for student in students:
                    if student['id'] == studentId:
                        subject['students'].append(studentId)
                        open(self.subjectFilepath, 'w').close()

                        with open(self.subjectFilepath, 'a') as f:
                            f.write("name,students")

                        for subject in subjects:
                            self.addSubject(Subject(subject['name'], [Student(s['id'], s['name'], s['age'], s['gender']) for s in students if s['id'] in subject['students']]))
                            return

                View.printError("Student not found")
                return
        View.printError("There is no subject with name '" + subjectName + "'.")








