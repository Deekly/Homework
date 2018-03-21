#   Homework #2
#   coded by Deekly
#   21.03.18

import random

print ("""
                    COIN THROW
""")

count = 0
heads = 0
tails = 0

input ("Press ENTER to start")

while count < 100:
    rand = random.randint(1,2)
    if rand == 1:
        print ("Heads!")
        heads += 1
        count += 1
    if rand == 2:
        print ("Tails!")
        tails += 1
        count += 1

print ("\n\nHEADS", heads)
print ("TAILS", tails)

input()
