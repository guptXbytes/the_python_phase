print("Welcome to the quiz! ")

playing = input("Do you want to play the quiz? \n 1.Yes 2.No " )
if playing.lower() != "yes":
    quit()

print("Thanks for Joining the quiz.")
score = 0

answer = input("What is full form of CPU? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is full form of GPU? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is full form of RAM? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is full form of ROM? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Thanks for attending the Quiz.")
print("You Scored " + str(score) + " Points in the quiz.")
print("Your Percentage was " + str((score/4) * 100) + "%.")

if score == 0:
    print("You failed the quiz.")
    
elif score != 4 : 
    print("You Passed the quiz")
else:
    print("You scored all the answers correct and passed the exam.")    