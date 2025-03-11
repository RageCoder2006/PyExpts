n = int(input("Enter the number to check: "))
sum = 0
temp = n
digits = len(str(n))

for i in str(n):
    sum += int(i) ** digits

if sum == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
