import random

higher_limit = input("Enter the number: ")

if higher_limit.isdigit():
    higher_limit = int(higher_limit)
    if higher_limit <=0:
        print("Enter a number greater than 0.")
        quit()
else:
    print("Try entering a number next time.")
    quit()        

random_number = random.randint(0,higher_limit)
guesses = 0 
while True:
    guesses +=1
    guess_number = input("Make a guess: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Try again by entering a number.")
        continue    
    if guess_number == random_number:
        print("You got it")
        break
    elif guess_number > random_number:
        print("You are higher the number")
    else:
        print("You are below the number")
    
print("You made it in",guesses,"guesses")        