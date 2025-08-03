class View:
    @classmethod
    def mainMenu(cls):
        print("""======= STUDENT MANAGER =======
1. Register a new student
2. Register a new subject
3. Enroll a student
4. Show all students
5. Show all subjects
        
0. Exit""")

        while True:
            try:
                return int(input("Enter your option: "))
            except:
                cls.printError("Invalid input.")


    @classmethod
    def printStudents(cls, students : list):
        print("======= STUDENTS =======")
        for student in students:
            print(f"{student['id']} - {student['name']} [Age: {student['age']} - gender: {student['gender']}]")

    @classmethod
    def printSubject(cls, subjects : list, students: list):
        print("======= SUBJECTS =======")
        for subject in subjects:
            print(f"{subject['name']} - Students: {[s['name'] for s in students if s['id'] in subject['students']]}")

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
