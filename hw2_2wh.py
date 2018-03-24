#   hw2_2wh
#   coded by Deekly
#   23.03.18

print("""
                    MIRROR INPUT

""")

word = input("Please input word(s)\n")
drow = ""

while word:
    drow += word[(len(word)-1)]
    word = word[:len(word)-1]
    

print("\n\nMirrored word is: ",drow)

input("END")
