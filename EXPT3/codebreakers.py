# Codebreakers App
import time

codes = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 11, "k": 12, "l": 13,
         "m": 14, "n": 15, "o": 16, "p": 17, "q": 18, "r": 19, "s": 21, "t": 22, "u": 23, "v": 24, "w": 25,
         "x": 26, "y": 27, "z": 28, " ": "~", ".": 31, "1": 32, "2": 33, "3": 34, "4": 35, "5": 36, "6": 37,
         "7": 38, "8": 39, "9": 41, "0": 42, "A": 10, "B": 20, "C": 30, "D": 40, "E": 50, "F": 60, "G": 70,
         "H": 80, "I": 90, "J": 110, "K": 120, "L": 130, "M": 140, "N": 150, "O": 160, "P": 170, "Q": 180,
         "R": 190, "S": 210, "T": 220, "U": 230, "V": 240, "W": 250, "X": 260, "Y": 270, "Z": 280, "=": "e",
         "+": "p", "-": "m", "?": "q"}


# Encrypt Function
def encrypt(msg):
    encrypt_list = []
    for letter in msg:
        if letter in codes:
            encrypt_list.append(str(codes[letter]))
        else:
            encrypt_list.append(letter)
    encrypted_msg = " ".join(encrypt_list)  # to put spaces in between
    print(f"Encrypted Message: {encrypted_msg}")


# Decrypt Function
def decrypt(encrypted_msg):
    encrypted_list = encrypted_msg.split()
    decrypted_list = []

    for i in encrypted_list:
        if i == "~":
            decrypted_list.append(" ")
        else:
            found = False
            for key, val in codes.items():
                if str(val) == i:
                    decrypted_list.append(key)
                    found = True
                    break
            if not found:
                decrypted_list.append("unk")

    decrypted_msg = "".join(decrypted_list)
    print(f"Decrypted Message: {decrypted_msg}")


def mainMenu():
    print("=========CodeBreakers=========")
    print("         MAIN MENU            ")
    print("Choose The Operation:")
    print("[a] Encode \n[b] Decode \n[c] Exit")
    choice = input(">>> ").strip().lower()

    if choice == "a":
        msg = input("Enter your message: ")
        encrypt(msg)
        print("Copy the message!")
        print("Redirecting to Main Menu")
        time.sleep(1)
        print()
        return True
    elif choice == "b":
        encrypted_msg = input("Enter the Encrypted Message: ")
        decrypt(encrypted_msg)
        print("Redirecting to Main Menu")
        time.sleep(1)
        print()
        return True
    elif choice == "c":
        print("Program Terminated!")
        return False
    else:
        print("Enter a valid choice!")
        time.sleep(1)
        print("Redirecting to Main Menu")
        time.sleep(1)
        print()
        return True


while True:
    if not mainMenu():
        break
