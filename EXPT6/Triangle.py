# type of triangle by number of sides

def identify(a, b, c):
    if a == b and b == c and c == a:
        print(f"The given triangle is an EQUILATERAL TRIANGLE of side {a}")
    elif (a == b and b == c) or (b == c and c == a) or (c == a and a == b):
        print(f"The given triangle is an ISOSCELES TRIANGLE of sides {a}, {b}, {c}")
    else:
        print(f"The given triangle is a SCALENE TRIANGLE of sides {a}, {b}, {c}")


a = int(input("Enter the side 1: "))
b = int(input("Enter the side 2: "))
c = int(input("Enter the side 3: "))

if (a, b, c) > (0, 0, 0):
    if (a + b) > c and (b + c) > a and (c + a) > b:
        identify(a, b, c)
    else:
        print("The given sides do NOT make a triangle! ")
else:
    print("The given sides do NOT make a triangle! ")
