#   hw4_c0mp_quessing
#   coded by Deekly
#   21.03.18 - 22.03.18


digit_start = 50
digit_var = 50
count = 0
answer = ""

player_number = int(input("For honest play input your number (it is honestly, i swear). Rememver, that computer doesn't know your number =)\n"))

while count != 9 or answer != "3":
    print ("Is it more or less than", digit_start, "?")
    answer = input("1. more 2. less 3. it is\n")
    if answer == "1" and digit_var > 1:
        count += 1
        digit_var = digit_var // 2
        digit_start = digit_start + digit_var
    if answer == "2" and digit_var > 1:
        count += 1
        digit_var = digit_var // 2
        digit_start = digit_start - digit_var
    if answer == "1" and digit_var <= 1:
        count += 1
        digit_var = 1
        digit_start = digit_start + digit_var
    if answer == "2" and digit_var <= 1:
        count += 1
        digit_var = 1
        digit_start = digit_start - digit_var
    if answer == "3":
        count += 1
        print ("ty!")
        break
    else:
        print ("please enter correct answer")
        continue
    print (digit_start)

print("c0mp count:", count)

if player_number == digit_start:
    print("HERE IT IS !!!!!!!!!!!!!!!")
if player_number != digit_start:
    print("YOU'RE CHEATER!!!")

input("END")
