import random
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
insBoard = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
NotOccupied = [1, 2, 3, 4, 5, 6, 7, 8, 9]
GameOver = False


def init():
    print("Lets Start with Tic Tac Toe")
    print("You play by choosing a number between 1-9 as per the position.\nShown by the Instruction board.")
    showInsBoard()
    print("If you want to see the Board again enter 0")


def showBoard():
    print()
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=' ')
        print()
    print()


def showInsBoard():
    print()
    for i in range(3):
        for j in range(3):
            print(insBoard[i][j], end=' ')
        print()
    print()


def CheckChoice(choice):
    if choice == 0:
        showInsBoard()
        return True
    elif 10 > choice > 0:
        err = makeMove(choice, 1)
        if err:
            return True
        else:
            return False
    else:
        print("Invalid Choice")
        playerChoice = int(input("Enter the Position you want to Choose by Enter a number from 1-9"))
        CheckChoice(playerChoice)


def makeMove(choice, player: int):
    if choice in NotOccupied:
        if 0 < choice < 4:
            index2 = insBoard[2].index(choice)
            board[2][index2] = player
        elif 3 < choice < 7:
            index2 = insBoard[1].index(choice)
            board[1][index2] = player
        else:
            index2 = insBoard[0].index(choice)
            board[0][index2] = player
        NotOccupied.remove(choice)
        return False
    else:
        return True


def computer():
    choice = None
    if len(NotOccupied) != 0:
        choice = random.choice(NotOccupied)
    makeMove(choice, 2)


def checkWinner():
    if board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] == 1:
            return 1
        elif board[0][0] == 2:
            return 2
    if board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] == 1:
            return 1
        elif board[1][0] == 2:
            return 2
    if board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] == 1:
            return 1
        elif board[2][0] == 2:
            return 2
    if board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] == 1:
            return 1
        elif board[0][0] == 2:
            return 2
    if board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] == 1:
            return 1
        elif board[0][1] == 2:
            return 2
    if board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] == 1:
            return 1
        elif board[0][2] == 2:
            return 2
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 1:
            return 1
        elif board[0][0] == 2:
            return 2
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 1:
            return 1
        elif board[0][2] == 2:
            return 2
    return -1


def gameOver():
    global GameOver
    if len(NotOccupied) == 0:
        GameOver = True
    winner = checkWinner()
    if winner == 1:
        print("Congratulation Player You Won!!")
        GameOver = True
    elif winner == 2:
        print("Computer Won!")
        GameOver = True
    if len(NotOccupied) == 0 and winner == -1:
        print("Its a Tie")


def main():
    
    while True:
        playerChoice = int(input("Enter the Position you want to Choose by Enter a number from 1-9"))
        loopCheck: bool = CheckChoice(playerChoice)
        if not loopCheck:
            break
    computer()
    showBoard()
    
    
init()
while not GameOver:
    main()
    gameOver()
