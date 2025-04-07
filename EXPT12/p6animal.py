class Animal:
    def sound():
        print("Animals make sound")

class Dog(Animal):
    def sound():
        print("Dogs bark")

Animal.sound()
Dog.sound()