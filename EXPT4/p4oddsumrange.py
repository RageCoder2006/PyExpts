start = int(input("Enter Lower Limit: "))
end = int(input("Enter Upper Limit: "))
sum = 0

for i in range(start, end + 1):
    if i % 2 != 0:
        sum += i

print(f"Sum of odd numbers from {start} to {end} is: {sum}")
