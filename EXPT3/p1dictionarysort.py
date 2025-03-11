data = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}


def sort_dict(d, reverse):
    items = list(d.items())
    direction = 1 if reverse else -1
    # using bubble sort algo here
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if (items[i][1] - items[j][1]) * direction > 0:
                items[i], items[j] = items[j], items[i]
    return dict(items)


print("Sorted in Ascending Order: ", sort_dict(data, True))
print("Sorted in Descending Order: ", sort_dict(data, False))
