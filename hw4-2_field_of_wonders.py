#   hw4_wonder_field

#   coded by Deekly
#   25.03.18 - 26.03.18

##  Terms of Reference (Техзадание):
##  
##  Создайте игру, в которой компьютер выбирает какое-либо слово,  а игрок должен его отгадать.
##  Компьютер сообщает игроку, сколько букв в слове, и даёт пять попыток узнать, есть ли какая-то буква в слове,
##  при чём компьютер может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово. 

import random


print("""
                             !!! WELCOME TO \"WONDRER FIELD\" !!!

                blah blah blah blah blah blah blah blah blah blah blah blah
                blah blah blah blah blah blah blah blah blah blah blah blah
                blah blah blah blah blah blah blah blah blah blah blah blah
                blah blah blah blah blah blah blah blah .... .... .... ....
    """)

##  Создает кортеж из слов. Потом будем выбирать случайное слово, угаданное слово исключать
WORDS = ("random","python","leonard","code","dragons","pistole")

##  вибирает случайное слово из WORDS
random_word_num = random.randrange(len(WORDS))
word = WORDS[random_word_num]

##  Выводит количество букв в загаданном слове
print("Word length is", len(word))


##  Цикл самой игры. Если игрок угадывает букву, открывается её позиция; иначе минус одна попытка (из пяти)
try_num = 0
while try_num != 5:

    ##  Ввод игроком буквы для проверки
    input_letter = input("Try to quess letter in word!\n")

    ##  Индекс буквы в слове для проверки на наличие её в слове
    letter_num = 0

    ##  Цикл проверки буквы на её наличие в слове
    while input_letter != word[letter_num]:
        letter_num += 1
        if letter_num == len(word):
            letter_num -= 1
            break

    ##  Если введенная игроком буква есть в слове, выводит текст    
    if input_letter == word[letter_num]:
        print("It is \"", input_letter, "\" in word. It stays", letter_num+1)
    else:
        try_num += 1
        print("No", input_letter, "in word\nYour count of tries is", 5-try_num)
        
    
    
print("You lost all tries. If you know all word, you can type it and win now. Or you can do mistake and lose. Or just press ENTER to quit")

last_chance = input()

if last_chance == word:
    input("YOU WIN!!!!!!!\nPress ENTER to quit")
if last_chance != word:
    input("YOU LOST!!!!!!\nPress ENTER to quit")
















































