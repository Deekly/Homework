#   hw3_word_jumble_v2
#   coded by Deekly
#   25.03.18


import random

print("""
                             !!! HELLO IN \"WORD JUMBLE\" !!!

                blah blah blah blah blah blah blah blah blah blah blah blah
                blah blah blah blah blah blah blah blah blah blah blah blah
                blah blah blah blah blah blah blah blah blah blah blah blah
                blah blah blah blah blah blah blah blah .... .... .... ....
    """)

##  Создает кортеж из слов. Потом будем выбирать случайное слово, угаданное слово исключать
WORDS = ("random","python","programming","code","imagination","hello world")

##  Создает переменную для общего счета в конце игры
total_score = 0

##  Цикл работает до тех пор, пока в кортеже WORDS есть слова
while WORDS:
    ##  Случайное число, по которому выбираем случайное слово из WORDS
    random_word_number = random.randrange(len(WORDS))

    ##  Переменная для определения кол-ва поинтов, заработанных игроком за отгаданное слово (только 2 или 3)    
    score = 0

    ##    Присваивает переменной word случайное слово из WORDS
    word = WORDS[random_word_number]
    
    ##  correct - переменная, в которой выбранное ранее слово для дальнейшей проверки. Только для проверки
    correct = word

    ##  Переменная для перемешивания букв в слове (word)  
    jumble = ""

    ##  Цикл перемешивания букв в слове (word)    
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position+1):]

    ##  Выводит уже перемешанное слово
    print("Jumbled word is:", jumble)

    ##  Попытка ввести правильное слово. Возможный ввод - правильное слово, неправильное слово, 1
    guess = input("\nTry to win!!!\nInput '1' to watch first letter\n")

    ##  Если ввод == 1, выводит подсказку (первую букву правильного слова), и отнимает 2 поинта (за подсказку)
    if guess == "1":
        print("First letter is:", correct[0])
        score -= 2
        guess = input()

    ##  Цикл новой попытки ввода правильного слова, если было введено неправильное. При пустом вводе идёт дальше
    while guess != correct and guess != "":
        print("You're wrong...")
        guess = input("Try to win!!!\n")

    ##  If-Else: если введено правильное слово, присваивает 3 поинта, если был пустой ввод, не присваивает ничего
    if guess == correct:
        score += 3
        print("GOOD JOB!!!")
    else:
        print("You're cheater!!!")
    
    ##  Инициализирует новый кортеж WORDS без отгаданного слова
    WORDS = WORDS[:random_word_number] + WORDS[(random_word_number+1):]

    ##  Конечный счёт. Выводится в конце игры    
    total_score += score

    
print("YOUR SCORE IS", total_score)
input("\n\nPress ENTER to quit")
