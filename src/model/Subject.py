from ..model.Student import Student

class Subject:
    def __init__(self, id:str, name:str):
        self.id = id
        self.name = name

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def setName(self, value):
        self.name = value

    def setId(self, value):
        self.id = value


