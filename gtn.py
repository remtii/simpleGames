# GUESS THE NUMBER
# 25/10/21
# BY REMTII
import random

x = random.randrange(1, 20)
win = False
print("Random number betweens 1 and 20")
while win == False:
    y = int(input("=] "))
    if y > x:
        print("Too big")
    elif y < x:
        print("Too small")
    elif y == x:
        print("You win! :D")
        win = True

