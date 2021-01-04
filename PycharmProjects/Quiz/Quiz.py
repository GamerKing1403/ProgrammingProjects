def question1():
    score1 = 0
    print("Q1) Which Of These Is Not A Browser ?")
    print("A) Facebook")
    print("B) Chrome")
    print("C) Firefox")
    print("D) Opera")
    ans = input("What Is the Answer ?")
    if ans == "A" or ans == 'a':
        score1 += 10
    elif ans == "B" or ans == 'b':
        score1 += 0
    elif ans == "C" or ans == 'c':
        score1 += 0
    elif ans == "D" or ans == 'd':
        score1 += 0
    else:
        print("You Did Some Thing Wrong")
    return score1


def question2():
    score2 = 0
    print("Q2) Who Is The CEO Of Google ?")
    print("A) Mark Zuckerburg")
    print("B) Sunder Pichai")
    print("C) Tim Cook")
    print("D) Bill Gates")
    ans = input("What Is the Answer?")
    if ans == "A" or ans == 'a':
        score2 += 0
    elif ans == "B" or ans == 'b':
        score2 += 10
    elif ans == "C" or ans == 'c':
        score2 += 0
    elif ans == "D" or ans == 'd':
        score2 += 0
    else:
        print("You Did Some Thing Wrong")
    return score2


ch = 'Y'
while ch == 'Y' or ch == 'y':
    score = question1()
    print()  # This IS For Next Line
    score += question2()
    print()  # This IS For Next Line
    print("Your Score is : ", score)
    print()  # This IS For Next Line
    if score == 20:
        print("Very Good Work You Answered All Answer Correctly!!!")
    elif score == 10:
        print("Good But You Need More Knowledge!!!")
    else:
        print("You Need To Work On Your G.K.")
    print()  # This IS For Next Line
    ch = input("Do You Want To Retry ?(Y for Yes And N for No)")
    print()  # This IS For Next Line
