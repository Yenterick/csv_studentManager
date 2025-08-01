import pprint as pp

class View:
    @classmethod
    def mainMenu(cls):
        print("""======= STUDENT MANAGER =======
1. Register a new student
2. Register a new subject
3. Enroll a student
        
0. Exit""")

        while True:
            try:
                return int(input("Enter your option: "))
            except:
                cls.printError("Invalid input.")


    @classmethod
    def printList(cls, name : str, list : list):
        print(f"======= {name} =======")
        pp.pprint(list)

    @classmethod
    def printError(cls, error : str):
        print(f" X - {error}")

    @classmethod
    def printInfo(cls, info : str):
        print(f" i - {info}")

    @classmethod
    def askString(cls, text : str):
        while True:
            try:
                return input(text)
            except:
                cls.printError("Invalid input.")

    @classmethod
    def askInt(cls, text : str):
        while True:
            try:
                return int(input(text))
            except:
                cls.printError("Invalid input.")
