class person:
    name = ""
    age = 0

    def __init__(self, n, a):
        self.name = n
        self.age = a

    def salary(self):
        pass

class emp(person):
    empID = ""
    def __init__(self,n, a, empid):
        super().__init__(n,a)
        self.empID = empid

    def salary(self):
        print("Salary Credited")

e1 = emp("abc",40,"12x2w34")
e1.salary()