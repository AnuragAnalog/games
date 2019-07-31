#!/usr/bin/python3

import random
import numpy as np

def cows(num: str, guess: str) -> None:
    cow = 0
    for i in range(len(num)):
        if num[i] == guess[i]:
            cow = cow + 1
    return cow

def bulls(num: str, guess: str) -> int:
    bull = 0
    n_list = [0 for i in range(10)]
    g_list = [0 for i in range(10)]

    for i in range(len(num)):
        n_list[int(num[i])] = n_list[int(num[i])] + 1
        g_list[int(guess[i])] = g_list[int(guess[i])] + 1

    for val1, val2 in zip(n_list, g_list):
        if val1 > 0 and val2 > 0 and val1 == val2:
            bull = bull + val1
        elif val1 > 0 and val2 > 0:
            bull = bull + np.abs(val1 - val2)
    return bull

def game(num: str) -> None:
    while True:
        guess = input("Enter your guess value: ")

        if num == guess:
            print("Congrats your guess is right.")
            break
        elif guess == "quit":
            print("Oops you have missed it,\nActual Number is", num)
            break
        elif len(num) != len(guess):
            print("Length of the guess value should be", len(num),"digits")
            continue
        cow = cows(num, guess)
        bull = bulls(num, guess)
        print(cow, "Cows", bull, "Bulls\n")

if __name__ == '__main__':
    print("To quit the game, type \"quit\"\n")
    num = random.randint(1,99999)
    num = str(num)
    print("Number of digits in the number is", len(num))

    game(num)