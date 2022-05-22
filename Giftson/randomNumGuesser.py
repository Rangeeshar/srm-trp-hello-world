"""
Python Program to guess the number within the range 1-10
Uses the library random

How to play?
enter a random number within 1-10 and the program will tell if you number is what you guessed
if its wrong, it`ll tell if the random number is lesser or greater than the number you guessed

Sample Run: >>>consider the random number to be 5

Please Guess the Number:
3
The number you entered is smaller
Please guess the number again
7
The number you entered is larger
Please guess the number again
5
You guessed it right! CongratZ!
5 is the correct number!!

"""
import random

# using randint function from the random library to generate integer values
# randint(1,10) produces a random value within the range of 1 to 10
randomNumber = random.randint(1, 10)

print("Please Guess the Number:")

# loop will continue to run until the break statement runs.
while True:
    guessingNumber = int(input())
    #
    if randomNumber < guessingNumber:
        print("Hint: The number you entered is larger\nPlease guess the number again")
    elif randomNumber == guessingNumber:
        print(
            f"You guessed it right! CongratZ!\n{randomNumber} is the correct number!!"
        )
        break
    else:
        print("Hint: The number you entered is smaller\nPlease guess the number again")
