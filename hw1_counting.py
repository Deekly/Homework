#   hw1_counting
#   coded by Deekly
#   23.03.18

print("\t\t\tCOUNTING")
start=int(input("Please input start of counting: "))
finish=int(input("Please input finish of counting: "))
delay=int(input("Please input delay: "))

for num in range(start, finish, delay):
    print(num)

input("Press ENTER to quit")
