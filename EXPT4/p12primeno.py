start = int(input("Starting Num: "))
end = int(input("Ending Num: "))

for num in range(start, end + 1):
    prime = True
    if num < 2:
        prime = False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
    if not prime:
        print(num)
