#!/usr/bin/python3

import random

def guess_the_number():
    print("I have a number, guess that\n")
    num = random.randint(1000)
    
    while True:
        guess = int(input("Guess the number: "))
        if guess > num:
            print("My number is smaller than yours\nTry Again")
        elif guess < num:
            print("My number is larger than yours\nTry Again")
        else:
            print("Hooray! You have guessed it right.")
            return
    
if __name__ == "__main__":
    guess_the_number()
