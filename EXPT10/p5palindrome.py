def palindrome(x):
    x = x.lower()
    if x == x[::-1]:
        print("Given String is Palindrome")
    else:
        print("NOT A Palindrome")

n = input("Enter a String: ")
palindrome(n)
