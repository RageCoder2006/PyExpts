class rectangle():
    length = 0
    breadth = 0

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        ar = self.length * self.breadth
        print(f"Area: {ar}")

    def perimeter(self):
        p = 2 * (self.length + self.breadth)
        print(f"Perimeter: {p}")


rect = rectangle(2, 4)
rectangle.area(rect)
rectangle.perimeter(rect)
