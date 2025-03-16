# Number Guessing Game
import random
import time


def secretNum():
    return random.randint(0, 50)


def checker(secret):
    while True:
        time.sleep(0.2)
        num = int(input("Enter Your Guess: "))
        if num == secret:
            time.sleep(0.5)
            print("CONGRATULATIONS, YOU'VE GUESSED THE NUMBER CORRECTLY!!!")
            time.sleep(1)
            break
        elif num < secret:
            time.sleep(0.2)
            print("Your guess is LOWER than the secret number")
        elif num > secret:
            time.sleep(0.2)
            print("Your guess is HIGHER than the secret number")


def mainMenu():
    print("==========Number Guessing Game==========")
    print("Press [A] to play or Press [X] to exit!")
    time.sleep(0.5)
    ch = input(">>> ")
    ch = ch.lower()
    if ch == "a":
        secret = secretNum()
        checker(secret)
        return True
    elif ch == "x":
        time.sleep(1)
        print("Program Terminated!")
        return False
    else:
        print("what????")
        time.sleep(2)
        print("Enter a valid response, dummy!")
        print()
        time.sleep(2)
        return True


while mainMenu():
    pass
