def collatzProblem(num):
    listOfSteps = []
    for i in range(2, num):
        numberOfSteps = 0
        newNum = i if i != 1 else i
        while newNum != 1:
            if newNum % 2 == 1:
                newNum = 3*newNum + 1
            else:
                newNum = newNum / 2
            numberOfSteps += 1
        listOfSteps.append(numberOfSteps)
        for j in [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]:
            if i == j:
                print(i)
    print(listOfSteps.index(max(listOfSteps)) + 2)
    return max(listOfSteps)+1


if __name__ == '__main__':
    while True:
        num = int(input("Enter the last Number You Want to check "))
        print(collatzProblem(num + 1))
        if input("Do You Want to Continue? ").lower() not in ['y', 'yes', 'ye']: break
