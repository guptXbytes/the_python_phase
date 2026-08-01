import random

user_wins = 0
comp_wins = 0
options = ["rock" , "paper" , "scissors"]

while True:
    user_option = input("Choose 1.rock, 2.paper, 3.scissors and 4.q for exit: ").lower()
    print("The user selected: ",user_option + ".")

    
    if user_option == "q":
        print("Exiting the game...")
        break
    if user_option not in options:
        print("Select a valid option!")
        continue
    comp_option = random.randint(0,2)
    print("The comp selected: ", options[comp_option] + ".")
    
    if user_option == "rock" and options[comp_option] == "scissors" :
        print("The user won the game!")
        user_wins +=1
    elif user_option == "scissors" and  options[comp_option] == "paper":
        print("The user won the game!")
        user_wins +=1
    elif user_option == "paper" and options[comp_option] == "rock":
        print("The user won the game!")
        user_wins +=1
    elif user_option == "rock" and options[comp_option] == "rock":
        print("It has been draw...") 
    elif user_option == "scissors" and options[comp_option] == "scissors":
            print("It has been draw...") 
    elif user_option == "paper" and options[comp_option] == "paper":
            print("It has been draw...")        
    else:
         print("You lost!!")
         comp_wins +=1                  
            
print("The number of user wins: ",user_wins)
print("The number of comp wins: ",comp_wins)
if user_wins > comp_wins:
     print("User is the WINNER!")
elif user_wins< comp_wins:
     print("Comp is the WINNER!")
else :
     print("It is a TIE!!")          