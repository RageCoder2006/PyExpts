class Person:
    fname = ""
    lname = ""

    def __init__(self, first, last):
        self.fname = first
        self.lname = last

    def greet(self):
        return f"Hello, my name is {self.fname} {self.lname}"


class Student(Person):
    sID = ""

    def __init__(self, fname, lname, stuid):
        super().__init__(fname, lname)
        self.sID = stuid

    def display_student_info(self):
        print("Student Name:", f"{self.fname} {self.lname}")
        print("Student ID:", f"{self.sID}")


p1 = Student("ABC", "DEF", 1234)
p1.greet()
p1.display_student_info()
