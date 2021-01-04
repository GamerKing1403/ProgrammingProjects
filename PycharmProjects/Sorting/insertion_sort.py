
if __name__ == '__main__':
    continuingVar = 'Y'
    checking = ['Y', 'YES', 'YE']
    while continuingVar in checking:
        userList = list(eval(input("Enter the list:- ")))
        for i in range(1, len(userList)):
            key = userList[i]
            j = i - 1
            while j >= 0 and key < userList[j]:
                userList[j+1] = userList[j]
                j = j - 1
            userList[j+1] = key
            print("The", i, "th Process Is :- ", userList)
        print("The List Is:- ", userList)
        continuingVar = input("Do You Want To Continue")
