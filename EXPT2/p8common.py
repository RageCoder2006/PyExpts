lst1 = ['banana', 'apple', 'orange', 'grapefruit', 'something']
lst2 = ['banana', 'mushroom', 'tomato', 'strawberry', 1]
out = False

for i in lst1:
    if i in lst2:
        out = True
        break
    else:
        continue

print(out)
