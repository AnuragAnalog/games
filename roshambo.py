#!/usr/bin/python3

# Rock paper scissors

import random

ROCK = 0
PAPER = 1
SCISSORS = 2
choices = [ROCK, PAPER, SCISSORS]
strings = {
    ROCK: 'Rock',
    PAPER: 'Paper',
    SCISSORS: 'Scissors'
}

UESR_WINS = 0
COMPUTER_WINS = 1
TIE = 2

USERS_SCORE = 0
COMPUTERS_SCORE = 0


def getResult(usersPick, computersPick):
    if computersPick == usersPick:
        return TIE

    if usersPick == ROCK:
        if computersPick == PAPER:
            return COMPUTER_WINS
        if computersPick == SCISSORS:
            return UESR_WINS

    if usersPick == PAPER:
        if computersPick == SCISSORS:
            return COMPUTER_WINS
        if computersPick == ROCK:
            return UESR_WINS

    if usersPick == SCISSORS:
        if computersPick == PAPER:
            return UESR_WINS
        if computersPick == ROCK:
            return COMPUTER_WINS


def printScoreBoard():
    print(f"\t\x1b[34m ************************************\x1b[0m")
    print(f"\t|   Your Score  |  Computer's Score  |")
    print(f"\t|    -----------------------------   |")
    print(f"\t|       {USERS_SCORE}\t|\t{COMPUTERS_SCORE}            |")
    print(f"\t\x1b[34m ************************************\x1b[0m")


def printRules():
    print(f'Press {ROCK} to pick Rock')
    print(f'Press {PAPER} to pick Paper')
    print(f'Press {SCISSORS} to pick Scissors')
    print("Enter any character or hit CTRL + C to end the game")


def getComputersPick():
    choice = random.choice(choices)
    return choice


def endGame():
    print("\nThat was a nice game.")
    printScoreBoard()
    print("Exiting...")
    quit()


def getUsersPick():
    while True:
        try:
            choice = int(input("Choose one: "))
        except:
            endGame()

        if choice == "quit":
            endGame()

        if choice not in choices:
            print("Invalid Choice")
            print("You must pick one from ", choices)
            continue
        return choice


def roshambo():
    global USERS_SCORE, COMPUTERS_SCORE
    usersPick = getUsersPick()
    computersPick = getComputersPick()
    result = getResult(usersPick, computersPick)

    if result == UESR_WINS:
        print(
            f"Yay! You win. I picked \x1b[32m{strings[computersPick]}\x1b[0m")
        USERS_SCORE += 1
    elif result == COMPUTER_WINS:
        print(
            f"Oops..! You loose. I picked \x1b[32m{strings[computersPick]}\x1b[0m")
        COMPUTERS_SCORE += 1
    else:
        print(
            f"It is a TIE. We both picked \x1b[32m{strings[computersPick]}\x1b[0m")


def Main():
    printRules()
    while(True):
        printScoreBoard()
        roshambo()


if __name__ == "__main__":
    Main()
