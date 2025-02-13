N = int(input("Enter the number till which the sum is to be found: "))
sum = 0
for i in range(1, N + 1):
    sum += i

print(f"Sum upto {N} is: {sum}")
