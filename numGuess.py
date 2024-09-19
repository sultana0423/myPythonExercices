# Number Guessing Game: Create a game where the computer randomly selects a number, and the user has to guess it within a limited number of tries.
import random 
tries = 10
randomNum = random.randint(1,100)
print(randomNum)
print("Number Guessing Game")
print("Guess the random number between 1 and 100.")

while tries > 0:
    print(f"Number of tries: {tries}")
    userGuess = int(input("Your guess? : "))
    if userGuess == randomNum:
        print("Your guess is right!")
        break
    else:
        print("Guess again")
        tries = tries - 1
        
if tries == 0:
    print("You have 0 tries. Try again.")

