#!/usr/bin/python3

import random

num = random.randint(1,99999)
num = str(num)
print("Number of digits in the number is", len(num)) 

def cows(num, guess):
    cow = 0
    for i in range(len(num)):
        if num[i] == guess[i]:
            cow = cow + 1
    print("Cows:", cow)

def bulls(num, guess):
    bull = 0
    for i in range(len(guess)):
        for j in range(len(num)):
            if num[j] == guess[i]:
                bull = bull + 1
                break
    print("Bulls:", bull)

while True:
    guess = input("Enter your guess value: ")
    guess = str(guess)

    if num == guess:
        print("Congrats your guess is right.")
        break
    elif guess == "quit":
        break
    elif len(num) != len(guess):
        print("Length of the guess value should be", len(num),"digits")
        break
    cows(num, guess)
    bulls(num, guess)
