#!/usr/bin/python3

import random

print("I have a number 1-1000, guess it!\n")
num = random.randint(1, 1000)
print(num)
numberOfTrys=0
higher=1000
lower=1
guess = 0
    
while guess != num:
    guess = int(input(f"Guess the number between {lower} and {higher}: "))
    numberOfTrys += 1
        
    if guess < lower or guess > higher:
        print("Your guess is not in range\n Try Again")
            
    elif guess > num:
        print("My number is smaller than yours\nTry Again")
        higher = guess
            
    elif guess < num:
        print("My number is larger than yours\nTry Again")
        lower = guess
            
    elif guess == num:
        print(f"Hooray! You have guessed {num} right in {numberOfTrys} attempt(s).")
            
