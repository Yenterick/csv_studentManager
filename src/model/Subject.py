from ..model.Student import Student

class Subject:
    def __init__(self, name:str, students:list[Student] = []):
        self.name = name
        self.students = students

    def getName(self):
        return self.name

    def getStudents(self):
        return self.students

    def setName(self, value):
        self.name = value

    def setStudents(self, value):
        self.students = value


