import random
import time

x = int(input("Enter the number: "))
win = False
m = x * 2
n = 1

while win == False:
    y = random.randrange(n, m)
    print("┌:] "+str(y))
    time.sleep(1)
    if y > x:
        print("└Too big")
        m = y - 1
    elif y < x:
        print("└Too small")
        n = y + 1
    elif y == x:
        print("└Computer win! :D")
        win = True

    if m == n or n == m:
        m += 1
    time.sleep(1)

