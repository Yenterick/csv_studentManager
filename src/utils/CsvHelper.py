from ..model.Student import Student
from ..model.Subject import Subject


class CsvHelper:
    def __init__(self, studentFilepath: str, subjectFilepath: str, registrationFilepath: str):
        self.studentFilepath = studentFilepath
        self.subjectFilepath = subjectFilepath
        self.registrationFilepath = registrationFilepath

    def loadAll(self):
        students = []
        subjects = []
        registrations = []

        with open(self.studentFilepath, 'r') as f:
            for i, line in enumerate(f.readlines()):
                student = line.strip().split(',')
                if i > 0:
                    students.append({
                        "id": student[0],
                        "name": student[1],
                        "age": int(student[2]),
                        "gender": student[3],
                        "subjects": []
                    })

        with open(self.subjectFilepath, 'r') as f:
            for i, line in enumerate(f.readlines()):
                subject = line.strip().split(',')
                if i > 0:
                    subjects.append({
                        "id": subject[0],
                        "name": subject[1],
                        "students": []
                    })

        with open(self.registrationFilepath, 'r') as f:
            for i, line in enumerate(f.readlines()):
                registration = line.strip().split(',')
                if i > 0:
                    registrations.append({
                        "subjectId": registration[0],
                        "studentId": registration[1]
                    })

        for r in registrations:
            student = next((s for s in students if s["id"] == r["studentId"]), None)
            subject = next((sub for sub in subjects if sub["id"] == r["subjectId"]), None)

            if student and subject:
                student["subjects"].append(subject["name"])
                subject["students"].append(student["name"])

        return students, subjects, registrations

    def addStudent(self, student: Student):
        studentString = '\n' + str(student.getId()) + "," + str(student.getName()) + "," + str(student.getAge()) + "," + str(student.getGender())
        with open(self.studentFilepath, 'a') as f:
            f.write(studentString)

    def addSubject(self, subject: Subject):
        subjectString = '\n' + str(subject.getId()) + "," + (subject.getName())
        with open(self.subjectFilepath, 'a') as f:
            f.write(subjectString)

    def enrollStudent(self, subject: Subject, student: Student):
        registrationString = '\n' + subject.getId() + "," + student.getId()
        with open(self.registrationFilepath, 'a') as f:
            f.write(registrationString)

    def editStudent(self, students, studentId, newName, newAge, newGender):
        for student in students:
            if student["id"] == studentId:
                student["name"] = newName
                student["age"] = newAge
                student["gender"] = newGender
                break

        with open(self.studentFilepath, "w") as f:
            f.write("id,name,age,gender")
            for s in students:
                line = f'\n{s["id"]},{s["name"]},{s["age"]},{s["gender"]}'
                f.write(line)

    def editSubject(self, subjects, subjectId, newName):
        for subject in subjects:
            if subject["id"] == subjectId:
                subject["name"] = newName
                break

        with open(self.subjectFilepath, "w") as f:
            f.write("id,name")
            for s in subjects:
                line = f'\n{s["id"]},{s["name"]}'
                f.write(line)

    def deleteStudent(self, students, registrations, studentId):
        students = [s for s in students if s["id"] != studentId]
        registrations = [r for r in registrations if r["studentId"] != studentId]

        with open(self.studentFilepath, "w") as f:
            f.write("id,name,age,gender")
            for s in students:
                line = f'\n{s["id"]},{s["name"]},{s["age"]},{s["gender"]}'
                f.write(line)

        with open(self.registrationFilepath, "w") as f:
            f.write("subjectId,studentId")
            for r in registrations:
                line = f'\n{r["subjectId"]},{r["studentId"]}'
                f.write(line)

    def deleteSubject(self, subjects, registrations, subjectId):
        subjects = [s for s in subjects if s["id"] != subjectId]
        registrations = [r for r in registrations if r["subjectId"] != subjectId]

        with open(self.subjectFilepath, "w") as f:
            f.write("id,name")
            for s in subjects:
                line = f'\n{s["id"]},{s["name"]}'
                f.write(line)

        with open(self.registrationFilepath, "w") as f:
            f.write("subjectId,studentId")
            for r in registrations:
                line = f'\n{r["subjectId"]},{r["studentId"]}'
                f.write(line)

    def deleteEnrollment(self, subjectId, studentId):
        with open(self.registrationFilepath, 'r') as f:
            lines = f.readlines()

        registrations = [line.strip().split(',') for line in lines[1:] if line.strip()]
        registrations = [r for r in registrations if not (r[0] == subjectId and r[1] == studentId)]

        with open(self.registrationFilepath, 'w') as f:
            f.write("subjectId,studentId")
            for r in registrations:
                line = '\n' + ','.join(r)
                f.write(line)
