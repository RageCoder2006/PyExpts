p = input("Enter Your Password: ")
valid = False

if len(p) >= 8:
    has_digit = False
    has_upper = False
    has_lower = False
    has_special = False

    for char in p:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char in "!@#$%^&*()-_+=<>?/":
            has_special = True

    if has_digit and has_upper and has_lower and has_special:
        valid = True

if valid:
    print("Valid Password")
else:
    print("Invalid Password")
