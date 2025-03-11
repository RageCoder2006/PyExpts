lst = []
sum = 0
lenlst = int(input("Enter The length of the list: "))
for j in range(0, lenlst):
    n = int(input("Enter the element: "))
    lst.append(n)
print(f"Input List: {lst}")

for i in lst:
    sum = sum + int(i)

print(f"Sum of the elements in the list is: {sum}")
