import random
def number_guesser():
    print("Welcome to the Number Guessing Game !! ")

lower = int(input("Enter the lower bound oh the range : "))
upper = int(input("Enter the upper bound of the range : "))

secret_num = random.randint(lower , upper)
attempts = 0

print(f"I have choosen a number between the {lower} and the {upper}. Lets guess it ! ")

while True:
    guess = int(input("Enter the number that you have guesed : "))
    attempts += 1

    if guess < secret_num:
        print("You guessed too Low . Please guess again.")
    elif guess > secret_num:
        print("You guess too High . Please guess again. ")       
    else:
        print(f"HURRAY ! CONGRATULATIONS !! You guessed the number {secret_num} correctly in {attempts} attempts . ") 
        break