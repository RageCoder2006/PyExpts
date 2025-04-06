class Person:
    fname = ""
    lname = ""
    def __int__(self,first, last):
        self.fname = first
        self.lname = last

    def greet(self):
        return f"Hello, my name is {self.fname} {self.lname}"

class Student(Person):
    sID = ""
    def __init__(self, fname, lname, stuID):
        super().__init__(fname,lname)
        self.sID = stuID

