import random


# This is the First Game
def game1(lower_limit, upper_limit, max_attempts):
    crt_ans = random.randint(lower_limit, upper_limit)  # This is the Correct Ans
    ch = 'Y'
    count = 1
    while ch == 'Y' or ch == 'y':
        your_ans = input(
            "Please Guess A Number Between " + str(lower_limit) + " and " + str(upper_limit))  # users Ans
        try:  # exceptions
            if int(your_ans) == crt_ans:  # checking
                print("You Are Correct!!")
                print("You did it in", count, "Tries")
                ch = 'N'
            elif int(your_ans) < crt_ans:
                print("Your Ans Is Smaller")
                print("Try Again")
                count += 1
            else:
                print("Your Ans Is Larger")
                print("Try Again")
                count += 1
        except():
            print("Please Enter a Number")
        if count == max_attempts:
            print("Oops You Failed!! The Correct Answer is :- ", crt_ans)
            ch = 'N'


# This is the second game
def game2():
    print("Hint:- My Favorite Number is Between 0 to 100")
    my_fav = 69
    ch = 'Y'
    count = 1
    while ch == 'Y' or ch == 'y':
        your_ans = input("What Do You Think it is?")
        try:
            if int(your_ans) == my_fav:
                print("You Are Correct!!!. You Did it in", count, "Tries")
                ch = 'N'
                if count == 1:
                    print("Damn You know Me Well!!!")
            else:
                print("Try Again")
                count += 1
        except():
            print("Please Enter A Number Between 0 to 100")


# This is the 3rd Game
def game3(game_level):
    if game_level == 'A' or game_mode == 'a':
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
                     'x', 'y', 'z']
        ctr_ans = alphabets[random.randint(0, 25)]
        ch = 'Y'
        count = 1
        while ch == 'Y' or ch == 'y':
            your_ans = input("Please Guess An Alphabet:- ")
            if your_ans in alphabets and your_ans == ctr_ans:
                print("You Are Correct!!!!. You Did it in", count, "Tries")
                ch = 'N'
            elif your_ans in alphabets and your_ans != ctr_ans:
                print("You Are Wrong Try Again!!")
                count += 1
                if alphabets.index(your_ans) < alphabets.index(ctr_ans):
                    print("The Correct Answer is Among The Letters That Comes After", your_ans)
                elif alphabets.index(your_ans) > alphabets.index(ctr_ans):
                    print("The Correct Answer is Among The Letters That Comes Before", your_ans)
    elif game_level == 'B' or game_level == 'b':
        vowels = ['a', 'e', 'i', 'o', 'u']
        ctr_ans = vowels[random.randint(0, 4)]
        ch = 'Y'
        count = 1
        while ch == 'Y' or ch == 'y':
            your_ans = input("Please Guess A Vowel:- ")
            if your_ans in vowels and your_ans == ctr_ans:
                print("You Are Correct!!!!. You Did it in", count, "Tries")
                ch = 'N'
            elif your_ans in vowels and your_ans != ctr_ans:
                print("You Are Wrong Try Again!!")
                count += 1
                if vowels.index(your_ans) < vowels.index(ctr_ans):
                    print("The Correct Answer is Among The Vowel That Comes After", your_ans)
                elif vowels.index(your_ans) > vowels.index(ctr_ans):
                    print("The Correct Answer is Among The Vowel That Comes Before", your_ans)


# This is the Fourth Game.
def game4():
    question = open("Question.txt", "r")
    questions = []
    qs = list(question.readlines())
    for x in qs:
        questions.append(x)
    random.shuffle(questions)
    answer = open("Answers.txt", "r")
    ans = list(answer.readlines())
    answers = {}
    for x in range(5):
        answers[qs[x]] = ans[x]
    crt_ans_str = "A D A B C"
    crt_ans = dict(zip(qs, crt_ans_str.split()))
    answer.close()
    question.close()
    points = 0
    for a in range(5):
        ques = questions[a]
        print(a+1, ")", ques, sep="")
        print(answers[ques])
        your_ans = input("Please Give the Answer(Answer Must Be In Caps):-")
        if your_ans == crt_ans[ques]:
            print("You Are Correct!!")
            points += 10
        else:
            print("You Are Wrong!!")
    print("Your Score is:-", points)

    if points == 0:
        print("You Did Poorly")
    if points == 10:
        print("You Need More Knowledge")
    elif points == 20:
        print("You Did Fairly Well")
    elif points == 30:
        print("You Did Good")
    elif points == 40:
        print("You Did Very Well")
    elif points == 50:
        print("Congratulation!!! You did This Without any Mistakes")


if __name__ == '__main__':
    ch2 = 'Y'
    while ch2 == 'Y' or ch2 == 'y':
        game_type = input('''What Do you Want To play?
        A)Guess A Random Number
        B)Guess My Favorite Number
        C)Guess A Random Alphabet
        D)Quiz
        (Please Type A,B,C or D)''')
        if game_type == "A" or game_type == 'a':
            game_difficulty = input("Please Enter The Difficulty You Want from Easy,Medium,Hard,Extreme or Impossible")
            if game_difficulty == "Easy" or game_difficulty == "easy":
                game1(0, 10, 5)
            elif game_difficulty == "Medium" or game_difficulty == "medium":
                game1(0, 100, 20)
            elif game_difficulty == "Hard" or game_difficulty == "hard":
                game1(0, 1000, 80)
            elif game_difficulty == "Extreme" or game_difficulty == "extreme":
                game1(0, 10000, 320)
            elif game_difficulty == "Impossible" or game_difficulty == "impossible":
                game1(0, 10000, 320)
            else:
                print("Please Enter One of those")
        elif game_type == 'B' or game_type == 'b':
            game2()
        elif game_type == 'C' or game_type == 'c':
            game_mode = input('''Please Select Any one of the Game:
            A)Guess The Alphabets(Medium)
            B)Guess The Vowel(Easy)''')
            game3(game_mode)
        elif game_type == 'D' or game_type == 'd':
            game4()
        ch2 = input("Do you Want to Continue??(Y for Yes And N for NO)")
