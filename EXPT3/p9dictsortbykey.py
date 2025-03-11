data = {'b': 1, 'a': 2, 'c': 3}

sorted_dict = {}
keys = list(data.keys())

for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        if keys[i] > keys[j]:
            keys[i], keys[j] = keys[j], keys[i]

for key in keys:
    sorted_dict[key] = data[key]

print("Sorted in Ascending Order: ", sorted_dict)
