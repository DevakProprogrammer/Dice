# importing all the things
import random


# dont add while loop now its a common mistake i already did and i was wondering why it was not working it took 30 mins of my life
again = True

while again:
    print(random.randint(1, 6))
    another_roll = input("Want to roll the dice again?(y/n):")
    if another_roll.lower() == "y":
        continue
    else:
        break