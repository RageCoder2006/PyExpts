data = {'a': 2, 'b': 3, 'c': 4}

prod = 1
for key in data:
    prod *= data[key]

print(f"Product of items is: {prod}")
