n = int(input("Enter the number to find factorial of: "))
fact = 1
if n == 0:
    fact = 1
else:
    for i in range(1, n + 1):
        fact = fact * i
print(f"Factorial of {n} is {fact}")
