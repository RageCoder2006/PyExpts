inp = int(input("Enter the Number: "))
inptstr = str(inp)
sum = 0

for i in inptstr:
    sum += int(i)

print(f"Sum of digits of the number {inp} is: {sum}")
