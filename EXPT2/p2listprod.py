lst = []
prod = 1
lenlst = int(input("Enter The length of the list: "))

for j in range(0, lenlst):
    n = int(input("Enter the element: "))
    lst.append(n)

print(f"Input List: {lst}")
for i in lst:
    prod = prod * int(i)

print(f"Product of the elements in the list is: {prod}")
