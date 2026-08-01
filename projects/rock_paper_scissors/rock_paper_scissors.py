import random

user_wins = 0
comp_wins = 0
options = ["rock" , "paper" , "scissors"]

while True:
    user_option = input("Choose 1.rock, 2.paper, 3.scissors and 4.q for exit: ").lower()
    comp_option = random.randint(0,2)
    if user_option == "q":
        print("Exiting the game...")
        break
    elif user_option in options:
        if user_option == "rock" and options[comp_option] == "scissors" :
            print("The user won the game!")
            user_wins +=1
        elif user_option == "scissors" and  options[comp_option] == "paper":
            print("The user won the game!")
            user_wins +=1
        elif user_option == "paper" and options[comp_option] == "rock":
            print("The user won the game!")
            user_wins +=1   
            
