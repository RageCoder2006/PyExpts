lst = list(input("Enter List: "))
prod = 1

for i in lst:
    prod = prod * int(i)

print(f"Product of the elements in the list is: {prod}")
