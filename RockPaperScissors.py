
# Rock, Paper, Scissors Game: Implement the classic rock, paper, scissors game where the user plays against the computer.
import random
print("Rock, Paper, Scissors Game")
print("1- Rock")
print("2- Paper")
print("3- Scissors")
randomPick = random.randrange(1,3)
userI = int(input("Your pick: "))

rock = randomPick == 1
paper = randomPick == 2
scissor = randomPick == 3

if userI == 1 and rock:
    print("Computer: Rock")
    print("You: Rock")
    print("Try again")
elif userI == 2 and  paper:
    print("Computer: Paper")
    print("You: Paper")
    print("Try again")
elif userI == 3 and scissor:
    print("Computer: Scissor")
    print("You: Scissor")
    print("Try again")
else:
    if userI == 1 and scissor:
        print("Computer: Scissor")
        print("You: Rock")
        print("You Win!")
    elif userI == 2 and rock:
        print("Computer: Rock")
        print("You: Paper")
        print("You Win!")
    elif userI == 3 and paper:
        print("Computer: Paper")
        print("You: Scissor")
        print("Computer Wins!")
    elif userI == 3 and rock:
        print("Computer: Rock")
        print("You: Scissor")
        print("Computer Wins!")
    elif userI == 1 and paper:
        print("Computer: Paper")
        print("You: Rock")
        print("Computer Wins!")
    elif userI == 2 and scissor:
        print("Computer: Scissor")
        print("You: Rock")
        print("Computer Wins!")
    else: 
        print("Choose a valid choice.")

print("Game is done.")
    
