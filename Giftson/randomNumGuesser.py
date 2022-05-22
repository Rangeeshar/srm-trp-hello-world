"""
Python Program to guess the number within the range 1-10
Uses the library random
Program Exp
"""
import random

# using randint function from the random library to generate integer values
# randint(1,10) produces a random value within the range of 1 to 10
n = random.randint(1, 10)

print("Please Guess the Number!")

# loop will continue to run until the break statement runs.
while True:
    o = int(input())
    if n < o:
        print("The number you entered is larger\n Please guess the number again")
    elif n == o:
        print(f"You guessed it right! CongratZ! {n} was the number.")
        break
    else:
        print("The number you entered is smaller\n Please guess the number again")
