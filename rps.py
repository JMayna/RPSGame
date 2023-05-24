import random

# Welcome the User
print("Hello and Welcome to Jordan's Rock, Paper, Scissors Game!")

# Prompt the user for their choice of Rock, Paper, or Scissors
validChoices = ["rock", "paper", "scissors"]
computerChoice = random.choice(validChoices)

while True:
    userChoice = input("Choose: Rock, Paper, or Scissors: ")
    if userChoice.lower() in validChoices:
        break
    else:
        print("Please enter 'rock', 'paper', or 'scissors'.")

# Compare choices and determine the winner
if userChoice == "paper" and computerChoice == "rock":
    print("You win! The computer chose", computerChoice)
elif userChoice == "paper" and computerChoice == "paper":
    print("Tie! The computer chose", computerChoice)
elif userChoice == "rock" and computerChoice == "paper":
    print("You lost! The computer chose", computerChoice)
elif userChoice == "rock" and computerChoice == "scissors":
    print("You win! The computer chose", computerChoice)
elif userChoice == "rock" and computerChoice == "rock":
    print("Tie! The computer chose", computerChoice)
elif userChoice == "scissors" and computerChoice == "paper":
    print("You win! The computer chose", computerChoice)
elif userChoice == "scissors" and computerChoice == "rock":
    print("You lost! The computer chose", computerChoice)
elif userChoice == "scissors" and computerChoice == "scissors":
    print("Tie! The computer chose", computerChoice)
