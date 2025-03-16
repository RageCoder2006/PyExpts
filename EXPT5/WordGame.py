import random

words = [
    "planet", "banana", "castle", "purple", "python", "guitar",
    "rocket", "jungle", "mirror", "sunset", "tunnel", "forest",
    "pencil", "diamond", "island", "laptop", "garden", "wizard",
    "bridge", "shadow"
]

secret = random.choice(words)


def game():
    ctr = 0
    print("======== Guess the Word Game ========")
    print(f"Hint: The word has {len(secret)} letters.")

    while True:
        guess = input("Enter Your Guess! ")
        guess = guess.lower()

        if guess == secret:
            print("Congratulations, You've WON the Game!")
            break
        else:
            print(f"Wrong guess! Hint: The word starts with '{secret[ctr]}'.")
            ctr += 1
            if ctr == len(secret):
                print(f"Oops, You Lost! The Word was {secret}")
                print("Better Luck Next Time! ")
                break


game()
