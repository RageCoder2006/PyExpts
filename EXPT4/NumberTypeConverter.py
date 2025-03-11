import time


def binary_to_decimal(binary):
    return str(int(binary, 2))


def decimal_to_binary(decimal):
    binary_value = bin(int(decimal))
    return binary_value[2:]


def decimal_to_hex(decimal):
    hex_value = hex(int(decimal))
    return hex_value[2:]


def hex_to_decimal(hex_val):
    return str(int(hex_val, 16))


def ascii_to_binary(text):
    binary_values = []
    for char in text:
        binary_values.append(format(ord(char), '08b'))
    return ' '.join(binary_values)


def binary_to_ascii(binary):
    binary_values = binary.split()
    ascii_text = ''
    for b in binary_values:
        ascii_text += chr(int(b, 2))
    return ascii_text


def mainMenu():
    print("========= Binary Data Converter =========")
    print("Choose the Operation:")
    print("[a] Binary to Decimal")
    print("[b] Decimal to Binary")
    print("[c] Decimal to Hexadecimal")
    print("[d] Hexadecimal to Decimal")
    print("[e] ASCII to Binary")
    print("[f] Binary to ASCII")
    print("[g] Exit")
    choice = input(">>> ").strip().lower()

    if choice == "a":
        binary = input("Enter Binary: ")
        print("Decimal:", binary_to_decimal(binary))
    elif choice == "b":
        decimal = input("Enter Decimal: ")
        print("Binary:", decimal_to_binary(decimal))
    elif choice == "c":
        decimal = input("Enter Decimal: ")
        print("Hexadecimal:", decimal_to_hex(decimal))
    elif choice == "d":
        hex_val = input("Enter Hexadecimal: ")
        print("Decimal:", hex_to_decimal(hex_val))
    elif choice == "e":
        text = input("Enter ASCII Text: ")
        print("Binary:", ascii_to_binary(text))
    elif choice == "f":
        binary = input("Enter Binary: ")
        print("ASCII Text:", binary_to_ascii(binary))
    elif choice == "g":
        print("Program Terminated!")
        return False
    else:
        print("Enter a valid choice!")

    time.sleep(1)
    print()
    return True


while True:
    if not mainMenu():
        break
