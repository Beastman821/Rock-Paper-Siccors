import random

play = int(input("What do you choose? type 0 for rock, 1 for paper, or 2 for scissors. "))

rps = [0, 1, 2,]

if play == 0:
    print("You choose rock")
elif play == 1:
    print("You Choose Paper")
elif play == 2:
    print("You Choose Siccors")
else:
    print("Invalid input you lose")

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print("The computer choose rock")
    if play == 1:
        print("Paper Covers Rock You Win")
    else:
        print("")
    if play == 2:
        print("Rock Crushes Siccors You Lose")
    else:
        print("")
elif computer_choice == 1:
    print("The computer Choose Paper")
    if play == 0:
        print("Paper Covers Rock You Lose")
    else:
        print("")
    if play == 2:
        print("Siccors Cuts Paper You Win")
    else:
        print("")
elif computer_choice == 2:
    print("The computer Choose Siccors")
    if play == 0:
        print("Rock Crushes Siccors You Win")
    else:
        print("")
    if play == 1:
        print("Siccors Cuts Paper You Lose")
    else:
        print("")
else:
    print("Invalid input")

if computer_choice == play:
    print("It's a Tie!!")
else:
    print("")

