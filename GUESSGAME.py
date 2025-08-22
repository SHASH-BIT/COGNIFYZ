#LEVEL 2
#GUESS IN GAME
import random

secret_num = random.randint(1,100)
attempts = 0
print("Welcome to the Number Guessing Game ! ")
print("I have choosen a number between 1 and 100 .")

while True:
    guess = int(input("Enter the number that you have guessed : "))
    attempts += 1

    if guess < secret_num:
        print("You guess too low . Please try again. ")
    elif guess > secret_num:
        print("You guess too high . Please try again. ")
    else:
        print(f"HURRAY ! CONGRATULATIONS ! You guessed it in {attempts} attempts . ")
        break