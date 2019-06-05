import random

print("Rock, Paper, Scissors, Shoot!")


# CAPTURE INPUTS
#  1. Create variables
#  2. Make it user friendly by repeating the choice.
user_choice = input("Please choose one of the following options 'rock', 'paper', or 'scissors' (without the quotes): ")
print("-------------")
print("You Chose: ", user_choice)


# VALIDATE INPUTS
#  3. Create a conditional statement and list to validate.

if user_choice not in ["rock", "paper", "scissors"]:
    print("INVALID SELECTION. PLEASE TRY AGAIN.")
    exit()

# GENERATE COMPUTER SELECTION
# 
print("GENERATING...")

computer_choice = random.choice(["rock", "paper", "scissors"])

print("--------------")
print("GENERATING...")
print("COMPUTER CHOICE:", computer_choice)

# DETERMINE THE WINNER
# 
# DISPLAY FINAL OUTPUTS / OUTCOMES