s = input("Enter something: ")
letters = 0
digits = 0

for char in s:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)
