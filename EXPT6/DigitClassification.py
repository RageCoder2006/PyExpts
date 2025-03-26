# digit based output class

num = int(input("Enter the number between 1 to 9,999: "))
count = 0
numog = num

while num > 0:
    num = num // 10
    count += 1

if count == 1 or numog == 0:
    print("Single Digit")
elif count == 2:
    print("Two Digits")
elif count == 3:
    print("Three Digits")
elif count == 4:
    print("Four Digits")
else:
    print("Out of Range")
