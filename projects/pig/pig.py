import random

def roll():
    min_value = 1
    max_value = 2
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit(): 
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

print("The total number of players are ", players)

max_score = 40
player_scores = [ 0 for _ in range(players)]

while max(player_scores) < max_score:
    should_roll = input("Would you like to roll (y/n)").lower()
    if should_roll is "y":
        break
    value = roll() 