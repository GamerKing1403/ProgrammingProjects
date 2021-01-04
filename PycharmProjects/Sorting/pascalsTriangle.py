
def spacing(length):
    space = ""
    for l in range(digits - length):
        space += " "
    return space


if __name__ == '__main__':
    while True:
        result = []
        firstTerm = [0, 1, 0]
        dummyVar = []
        result.append(firstTerm)
        n = 0
        while True:
            try:
                n = int(input("Enter the Number of lines You Want of the Pascals Triangle."))
                break
            except ValueError:
                print("Please Enter a Number")
                continue

        for i in range(n):
            dummyVar.append(0)
            for j in range(len(firstTerm) - 1):
                dummyVar.append(firstTerm[j] + firstTerm[j + 1])
            dummyVar.append(0)
            result.append(dummyVar)
            firstTerm = dummyVar
            dummyVar = []

        digits = len(str(max(result[len(result) - 1])))

        for i in range(len(result)):
            for k in range(n, i, -1):
                print(" ", end="")
            for j in range(len(result[i])):
                if result[i][j] != 0:
                    print(result[i][j], end=spacing(len(str(result[i][j])) - 1))
            print()

        ch = input("Continue?(Y/N)")
        if ch == 'Y' or ch == 'y':
            continue
        else:
            break
