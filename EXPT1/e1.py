# Area of Triangle

import math

print("Please select your input variables:")
print("[a] base and height \n[b] 3 sides \n[c] 2 sides and included angle")

ip_choice = input(">>>").lower()


def heron(a, b, c):
    semip = (a + b + c) / 2
    area = math.sqrt(semip * (semip - a) * (semip - b) * (semip - c))
    return area


if ip_choice == "a":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
elif ip_choice == "b":
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    side3 = float(input("Enter third side: "))
    area = heron(side1, side2, side3)
elif ip_choice == "c":
    side1 = float(input("Enter first side: "))
    side2 = float(input("Enter second side: "))
    angle = float(input("Enter the included angle in degrees: "))
    area = 0.5 * side1 * side2 * math.sin(math.radians(angle))
    print(math.sin(math.radians(angle)))
while True:
    try:
        print(f"Area of the triangle with given dimensions is: {area}")
        break
    except NameError:
        print("Select the option correctly")
        break