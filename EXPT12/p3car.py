class Car():
    make = ""
    model = ""
    year = 0000

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        print(f"Make: {self.make} \nModel: {self.model} \nYear: {self.year}\n")


car1 = Car("ABC", "XYZ", 2000)
car2 = Car("DEF", "RST", 2006)
Car.car_info(car1)
Car.car_info(car2)
