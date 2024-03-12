#importing required libraries
import random

#game name
game = "Hang Man"

#creating an empty list
word_bank = []

#opening the file and storing it in the list
with open("words.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        word = line.strip()
        word_bank.append(word)

#selecting a random word for==rom word_bank
q = random.choice(word_bank)

#defining variables for the conditions
misplaced_words = []
incorrect_words = []
total_trials = 5
current_trial = 0

#welcoming message
print(f"Welcome to {game}")
print(f"The word has {len(q)} letters.")
print(f"You have {total_trials-current_trial} trials left.")

#setting up game loop
while current_trial < total_trials:
    guess = input("What is your guess?").lower()

    #setting up condition
    if len(guess) != len(q) or not guess.isalpha():
        print("Please enter a 5 digit word.")
        continue

    index = 0
    for i in guess:
        if i == q[index]:
            print(i,end = "")
            if i in misplaced_words:
                misplaced_words.remove(i)
        elif i in q:
            if i not in misplaced_words:
                misplaced_words.append(i)
            print("_",end = "")
        else:
            if i not in incorrect_words:
                incorrect_words.append(i)
            print("_", end="")
        index += 1

    #printing the feedback of his trial
    print("\n")
    print("Misplaced Words: ",misplaced_words)
    print("Incorrect Words: ",incorrect_words)

    #increasing the trial by 1
    current_trial += 1

    #checking whether the player has won or not
    if guess == q:
        print("Hurray! You have won the game.")
        break
    elif current_trial > 4:
        print("Oops! You ran out of trials.")
        print("The correct answer is ",q)
        break
    else:
        print(f"You have {total_trials - current_trial} trials left.")