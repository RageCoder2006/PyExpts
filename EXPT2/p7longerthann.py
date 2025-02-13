lst = ['banana', 'apple', 'orange', 'grapefruit']
n = int(input("Enter n: "))
newlst = []
for i in lst:
    if len(i)>n:
        newlst.append(i)
    else:
        continue

print(f"Words longer than n from the given list are: {newlst}")