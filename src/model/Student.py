class Student:
    def __init__(self, id:str, name:str, age:int, gender:str):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__gender = gender

    def getId(self):
        return self.__id

    def setId(self, value):
        self.__id = value

    def getName(self):
        return self.__name

    def setName(self, value):
        self.__name = value

    def getAge(self):
        return self.__age

    def setAge(self, value):
        self.__age = value

    def getGender(self):
        return self.__gender

    def setGender(self, value):
        self.__gender = value



