def remdup(lst):
    newl = []
    for i in lst:
        if i not in newl:
            newl.append(i)
        else:
            continue
    lst = newl
    return lst

print(remdup([1,2,2,3,2,2,3,3,4,2,3]))

