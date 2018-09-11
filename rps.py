from random import randint
from time import sleep
user_choice = 0
computer_choice = 0
replay = 0
### something somethin something##


def computer_convert():
    global computer_choice
    computer_choice = randint(1, 3)
    if computer_choice == 1:
        computer_choice = "Rock"
    elif computer_choice == 2:
        computer_choice = "Sissors"
    elif computer_choice == 3:
        computer_choice = "Paper"


choices = ["Rock", "Paper", "Sissors"]

result = {
    "tie": "Fuckin Tie bro.",
    "won": "You did it mango, YOU WON!",
    "lost": "Totally NOT math. You lost.",
}

def decide_winner(user_choice, computer_choice):
    print("Contestants Set! Here we go!")
    sleep(3)
    print("Rock")
    sleep(1)
    print("Paper")
    sleep(1)
    print("Sissors")
    sleep(1)
    print("Go!")
    sleep(1)
    print()
    print()
    print(user_choice + " vs " + computer_choice)
    print()
    print()

def print_winner():
    if user_choice == computer_choice:
        print(result["tie"])
    elif user_choice == "Rock" and computer_choice == "Sissors":
        print(result["tie"])
    elif user_choice == "Paper" and computer_choice == "Rock":
        print(result["won"])
    elif user_choice == "Sissors" and computer_choice == "Paper":
        print(result["won"])
    elif user_choice == "Sissors" and computer_choice == "Rock":
        print(result["lost"])
    elif user_choice == "Rock" and computer_choice == "Paper":
        print(result["lost"])
    elif user_choice == "Paper" and computer_choice == "Sissors":
        print(result["lost"])

def play_again():
    global replay
    replay = input("Play Again? Enter Y or N: ").upper()
    if replay == "Y":
        play_rps()
    else:
        exit()

def play_rps():
    global user_choice
    user_choice = input("Please Select Rock, Paper, or Sissors: ").capitalize()
    computer_convert()
    decide_winner(user_choice, computer_choice)
    print_winner()
    print()
    play_again()
    print()

play_rps()