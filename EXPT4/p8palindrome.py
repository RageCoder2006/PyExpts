s = input("Enter the string to check: ")
n = len(s)
palindrome = True

for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        palindrome = False
        break

if palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")
