a = int(input("enter first number: "))
b = int(input("enter second number: "))

# method-1 using temp var
temp = a
a = b
b = temp
print(f"a = {a}, b = {b}")

# method-2 without using temp var
a = a + b
b = a - b
a = a - b
print(f"a = {a}, b = {b}")