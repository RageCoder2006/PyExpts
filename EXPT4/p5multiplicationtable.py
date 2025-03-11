# Multiplication table

num = int(input("Enter the number to generate the multiplication table: "))
lim = int(input("Enter the upper limit: "))

print(f"Multiplication Table of {num} up to {lim}:")

for i in range(1, lim + 1):
    print(f"{num} × {i} = {num * i}")
