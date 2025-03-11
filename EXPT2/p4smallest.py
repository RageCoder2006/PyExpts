lst = []
lenlst = int(input("Enter The length of the list: "))

for j in range(0, lenlst):
    n = int(input("Enter the element: "))
    lst.append(n)

print(f"Input List: {lst}")

lst.sort()

print(f"Smallest number in the given list is: {lst[0]}")
