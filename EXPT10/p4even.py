l = []
n = int(input("Enter the no. of elements: "))
for i in range(n):
    ele = int(input("Enter Element:"))
    l.append(ele)

even = filter(lambda x: x % 2 == 0, l)
print(list(even))
