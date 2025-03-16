num = int(input("Enter the Number: "))
numog = num
fact = 1

if num == 0:
    print(f"Factorial of {numog} is {fact}")
else:
    while num != 0:
        fact *= num
        num -= 1
    print(f"Factorial of {numog} is {fact}")
