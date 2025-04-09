import random

playerScore = 0


def user_choice():
    u_opt = {"r": "rock", "p": "paper", "s": "scissor"}
    userch = input("Enter Rock (R), Paper(P), or Scissor(S): ")
    userch = userch.lower()
    if len(userch) == 1:
        userch = u_opt[userch]
    else:
        userch = userch
    return userch


def game_loop():
    global playerScore
    options = ["rock", "paper", "scissor"]
    comp_choice = options[random.randint(0, 2)]
    player = user_choice()
    print(f"You chose: {player} and Computer chose: {comp_choice}")
    if player == comp_choice:
        print("Tie, Noone wins!")
    elif (player == "rock" and comp_choice == "scissor") or (player == "paper" and comp_choice == "rock") or (
            player == "scissor" and comp_choice == "paper"):
        print("You win!")
        playerScore += 1
    else:
        print("You lose!")
    print(f"\nYour score: {playerScore}\n")


def main_menu():
    gameVar = True
    roundNo = 1
    while gameVar:
        print("====== Rock, Paper, Scissors ======")
        print(f"Round No.: {roundNo}")
        print("press 'x' to play")
        print("Press 'q' to quit")
        game = input(">>> ")
        game = game.lower()
        if game == "x":
            game_loop()
            gameVar = True
        else:
            print("Bye!")
            gameVar = False
        roundNo += 1


main_menu()
