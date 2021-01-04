
if __name__ == '__main__':
    continuingVar = 'Y'
    checking = ['Y', 'YES', 'YE']
    while continuingVar.upper() in checking:
        userList = list(eval(input("Enter the list:- ")))
        countVar = 0
        for j in range(1, len(userList)):
            for i in range(0, len(userList)-1):
                if userList[i] > userList[i+1]:
                    userList[i], userList[i+1] = userList[i+1], userList[i]
                countVar += 1
                print("The", countVar, "th Process Is :- ", userList)
        print("The Sorted List Is :- ", userList)
        continuingVar = input("Do You Want To Continue")
