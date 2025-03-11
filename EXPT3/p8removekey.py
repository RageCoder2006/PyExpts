data = {'a': 1, 'b': 2, 'c': 3}

print(data)
key = input("Enter the key to delete: ")

if key in data:
    del data[key]

print(data)
