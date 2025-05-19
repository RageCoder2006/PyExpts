l1 = []

n = int(input("Enter Number of Elements in the list: "))
for i in range(n):
    ele = int(input(f"Enter Element #{i+1}: "))
    l1.append(ele)

def maxl(l):
    maxl = [0]
    for i in range(0,len(l)):
        if l[i] > maxl[0]:
            maxl[0] = l[i]
        else:
            continue

    print("Maximum Number in the given list is: ", maxl[0])

maxl(l1)
