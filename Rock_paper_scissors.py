import random

from art import rock,Paper,Scissors

Action=[rock, Paper, Scissors]

Player= int(input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))

print(Action[Player])

Computer= random.randint(0,2)

print("Computer chose :\n" + Action[Computer])

if Player == 0 :
    if Computer == 0:
        print("Equal")
    elif Computer == 1:
        print("You lose")
    else:
        print("You Win !!!")
elif Player == 1 :
    if Computer == 0 :
        print("You Win !!!")
    elif Computer == 1 :
        print("Equal")
    else:
        print("You lose")
else:
    if Computer == 0:
        print("You lose")
    elif Computer == 1:
        print("You Win !!!")
    else:
        print("Equal")


