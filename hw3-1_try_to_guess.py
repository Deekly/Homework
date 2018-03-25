#   hw3_try_to_guess
#   coded by Deekly
#   21.03.18

#   Try to guess my number from 1 to 100

import random

print ("""
                            !!! TRY TO GUESS !!!
                            
                        blah blah blah blah blah blah
                        blah blah blah blah blah blah
                        blah blah blah blah .... ....
""")

input ("\t\t\tPress enter if understood")

rand = random.randint(1,100)

print ("Lets start =)")
count = 0
digit = 0
print ("Enter Sandman:")    

while digit != rand:
    digit = int(input())
    if digit > rand:
        print ("Try less")
        count += 1
    if digit < rand:
        print ("Try more")
        count += 1
    if count == 10:
        break
if count < 10:
    print ("\t\t\t !!! YOU WIN !!!")
    print ("Your result:", count)
if count >= 10:
    print ("YOU LOSE")

input()
