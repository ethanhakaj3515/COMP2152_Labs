choices = ['rock', 'paper', 'scissors']

playerChoice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
playerChoice = playerChoice.replace(" ", "")


if playerChoice in choices:
    print(f"You chose {playerChoice}")
else:
    print("Invalid choice. Please enter rock, paper, or scissors.")

import random

computerChoice = random.choice(choices)
print(f"Computer chose {computerChoice}")

if playerChoice == computerChoice:
    print("It's a tie!")
elif (playerChoice == 'rock' and computerChoice == 'scissors'):
     print("Rock crushes scissors! You win!")
elif (playerChoice == 'paper' and computerChoice == 'rock'):
     print("Paper covers rock! You win!")
elif (playerChoice == 'scissors' and computerChoice == 'paper'):
     print("Scissors cuts paper! You win!")
else:
    print("Computer wins!")