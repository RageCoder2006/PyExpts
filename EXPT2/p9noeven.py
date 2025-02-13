lst = [2, 4, 1, 4, 5, 5, 9, 10]

for i in lst[:]:  # slice bcoz it creates a list copy, prevents skipping
    if i % 2 == 0:
        lst.remove(i)
    else:
        continue

print(lst)
