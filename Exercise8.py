'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock'''

import random

var=1
lis=['rock','paper','scissors']


while var:
    x=input("Rock-Paper-Scissors: ").lower()
    tes=random.choice(lis)
    if x==tes:
        print("Both chose {}".format(x))
    elif (x=='rock' and tes=='scissors') or (x=='scissors' and tes=='paper') or (x=='paper' and tes=='rock'):
        print("You won!")
    else:
        print("You lose!")
    n=int(input("Do you want to play again Yes(1) No(0): "))
    if not n:
        var=0




