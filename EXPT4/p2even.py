start = int(input("Enter Lower Limit: "))
end = int(input("Enter Upper Limit: "))

for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)
