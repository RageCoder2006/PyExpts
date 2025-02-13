duplst = ["banana","apple","orange","banana","orange","grapefruit","orange"]
revlst = []
for i in duplst:
    if i not in revlst:
        revlst.append(i)
    else:
        continue

print(f"Revised list after removing duplicates is: {revlst}")