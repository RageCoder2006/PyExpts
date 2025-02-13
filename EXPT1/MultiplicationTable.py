#Structured Multiplication Table Program

startno = int(input("Enter the Start Number: "))
endno = int(input("Enter the End Number: "))
upperlim = int(input("Enter the range for printing table: "))

for i in range(startno, upperlim + 1):
    print("", end=" ")
    for j in range(1, endno + 1):
        print(str(i * j).rjust(3), end=" ")
    print()
