class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        ar = 3.14*(self.radius**2)
        print(f"Area of the Circle is: {ar}")

    def circumference(self):
        cir = 2*3.14*(self.radius)
        print(f"Circumference of the Circle is: {cir}")

circle = Circle(7)
Circle.area(circle)
Circle.circumference(circle)
