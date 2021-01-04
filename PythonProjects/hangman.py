from collections import Counter
import random
lives = [1, 1, 1, 1, 1]
word = ""
guessWord = []
gameOver = False


def loadWord():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words


def setUpWord():
    global word, guessWord
    word = random.choice(loadWord())
    print(word)
    for i in word:
        guessWord.append("_")
    wordCounted = Counter(word)
    print(wordCounted)


def init():
    print("This is hangman Just type the letter you want to guess and if you get it correct then you will not lose any "
          "hearts and if get it wrong 1 heart will be lost.")
    print("In the next line you have to enter either a letter for the guess or 1 for instruction or 0 for the number "
          "of lives left.")
    setUpWord()


def userInput():
    guess = input("Enter The guess or 1 or 0:- ")
    if guess.isalpha():
        repeatation = wordCounted[guess]
        while repeatation > 0:
            checkWord(guess)
            repeatation -= 1
    elif guess.isnumeric() and int(guess) == 1:
        init()
    elif guess.isnumeric() and int(guess) == 0:
        showLives()
    else:
        print("Error")


def showBoard():
    for i in guessWord:
        print(i, end='')
    print()
    showLives()


def checkWord(guess):
    global guessWord
    toChange = guessWord[word.find(guess)]
    if guess in word and toChange == "_":
        guessWord[word.find(guess)] = guess
        return True
    else:
        lives.pop(len(lives)-1)
        return False


def showLives():
    for i in range(len(lives)):
        print('\u2764',  end='')
    print()


def checkEnd():
    global gameOver
    word2 = ''
    for letter in guessWord:
        word2 += letter
    if len(lives) == 0\
            :
        print("Game Over.\nYou Lost!")
        gameOver = True
    elif word2 == word:
        print("You Won!")
        gameOver = True


def main():
    init()
    while not gameOver:
        userInput()
        showBoard()
        checkEnd()


main()
