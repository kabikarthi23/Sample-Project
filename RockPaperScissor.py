#importing required libraries
from random import randint

#creating a list for computer
t=["Rock","Paper","Scissors"]

#make computer to choose random one from t
computer=t[randint(0,2)]

#setting player to false
player=False

#setting up score
score = 0

#setting up while loop
while player == False:
    player=input("Choose one:Rock,Paper,Scissors(To stop playing type Bored): ")

    #to convert the input infavour of us 
    a=len(player)
    b=str(player[0]).upper()
    c=str(player[1:a]).lower()
    player=b+c
    print()

    #setting up the condition
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose",computer,"covers",player)
        else:
            print("You win",player,"smashes",computer)
            score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose",computer,"cuts",player)
        else:
            print("You win",player,"covers",computer)
            score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose",computer,"smashes",player)
        else:
            print("You win",player,"cuts",computer)
            score += 1
    elif player == "Bored":
        print("Your Final Score: ",score)
        print("Bye! Come back later! ")
        break
    
    else:
        print("That's not a valid play. Check the spelling")

    print()
    #player is set to true
    #now setting player to false to contiue the loop
    player = False
    computer = t[randint(0,2)]
