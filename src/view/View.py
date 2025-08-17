class View:
    @classmethod
    def mainMenu(cls):
        print("""======= STUDENT MANAGER =======
1. Register a new student
2. Register a new subject
3. Enroll a student
4. Show all students
5. Show all subjects
6. Edit student
7. Edit subject
8. Delete student
9. Delete subject
10. Delete registration

0. Exit""")

        while True:
            try:
                return int(input("Enter your option: "))
            except:
                cls.printError("Invalid input.")

    @classmethod
    def printStudents(cls, students: list):
        print("======= STUDENTS =======")
        for student in students:
            subjects = ", ".join(student["subjects"]) if student["subjects"] else "None"
            print(f"{student['id']} - {student['name']} "
                  f"[Age: {student['age']} - Gender: {student['gender']}] "
                  f"=> Subjects: {subjects}")

    @classmethod
    def printSubjects(cls, subjects: list):
        print("======= SUBJECTS =======")
        for subject in subjects:
            students = ", ".join(subject["students"]) if subject["students"] else "None"
            print(f"{subject['id']} - {subject['name']} "
                  f"=> Students: {students}")

    @classmethod
    def printError(cls, error: str):
        print(f" X - {error}")

    @classmethod
    def printInfo(cls, info: str):
        print(f" i - {info}")

    @classmethod
    def askString(cls, text: str):
        while True:
            try:
                return input(text)
            except:
                cls.printError("Invalid input.")

    @classmethod
    def askInt(cls, text: str):
        while True:
            try:
                return int(input(text))
            except:
                cls.printError("Invalid input.")
