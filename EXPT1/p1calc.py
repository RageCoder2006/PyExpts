a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

add = a + b
sub = a - b
mul = a * b
while True:
    try:
        div = a / b
        break
    except ZeroDivisionError:
        div = "can not divide by zero"
        break

print("Addition Result = ", add)
print("Subtraction Result = ", sub)
print("Multiplication Result = ", mul)
print("Division Result = ", div)
