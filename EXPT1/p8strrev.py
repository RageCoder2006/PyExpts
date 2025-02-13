str = input("Enter a string: ")
revstr = ""
for i in range(-1, -len(str) - 1, -1):
    revstr += str[i]
print(revstr)
