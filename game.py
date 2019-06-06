import random

def my_message():
    return "HELLO"

# only if this script is executed from teh command-line
if __name__ == "__main__":
    
    print("Rock, Paper, Scissors, Shoot!")


    # CAPTURE INPUTS
    #  1. Create variables
    #  2. Make it user friendly by repeating the choice.
    user_choice = input("Please choose one of the following options 'rock', 'paper', or 'scissors' (without the quotes): ")
    print("-------------")
    print("You Chose: ", user_choice)


    # VALIDATE INPUTS
    #  3. Create a conditional statement and list to validate.

    valid_options = ["rock", "paper", "scissors"]

    if user_choice not in valid_options:
        print("INVALID SELECTION. PLEASE TRY AGAIN.")
        exit()

    # GENERATE COMPUTER SELECTION
    #  4. Add the "import random" to the top of the code
    #  5. Create a computer_choice variable to choose from the lsit at random.

    print("GENERATING...")

    computer_choice = random.choice(valid_options)

    print("--------------")
    print("GENERATING...")
    print("COMPUTER CHOICE:", computer_choice)

    # DETERMINE THE WINNER
    #  6. Create conditional logic with possible outcomes:
    #     - rock beats scissors
    #     - paper beats rock
    #     - scissors beats paper
    #     - same selections is a tie

    # MY WORKING VERSION
    #'''if user_choice == computer_choice:
    #'''    print("  TIE, BABY. EVERYONE'S A WINNER!")
    #'''elif user_choice == "rock" and computer_choice == "paper":
    #'''    print("  COMPUTER WINS. ROCK < PAPER. SORRY!")
    #'''elif user_choice == "rock" and computer_choice == "scissors":
    #'''    print("  YOU WIN. ROCK > SCISSORS. HOORAY!")
    #'''elif user_choice == "paper" and computer_choice == "scissors":
    #'''    print("  COMPUTER WINS. PAPER < SCISSORS. SORRY!")
    #'''elif user_choice == "paper" and computer_choice == "rock":
    #'''    print("  YOU WIN.  PAPER > ROCK. HOORAY!")
    #'''elif user_choice == "scissors" and computer_choice == "rock":
    #'''    print("  COMPUTER WINS. SCISSORS < ROCK. SORRY!")
    #'''elif user_choice == "scissors" and computer_choice == "rock":
    #'''    print("  YOU WIN. SCISSORS > PAPER. SHOORAY!")

    # DISPLAY FINAL OUTPUTS / OUTCOMES

    #print("THANKS FOR PLAYING. PLEASE PLAY AGAIN!")


    # PROFESSOR'S VERSION: first attribute represents the user, second represents the computer
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }

    winning_choice = winners[user_choice][computer_choice]

    # DISPLAY FINAL OUTPUTS / OUTCOMES

    if winning_choice:
        if winning_choice == user_choice:
            print("YOU WON")
        elif winning_choice == computer_choice:
            print("YOU LOST")
    else:
        print("TIE")

    print("Thanks for playing. Please play again!")