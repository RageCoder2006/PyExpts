string = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""
i = 0

while i < len(string):
    if string[i] not in vowels:
        result += string[i]
    i += 1

print("String without vowels:", result)