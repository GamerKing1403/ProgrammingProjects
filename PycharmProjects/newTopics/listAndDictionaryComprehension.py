# List Comprehension:-

# Function for checking if a list is in another list
def checkListInOneAnother(listToCheck , listToCheckFrom ):
    for i in listToCheckFrom:
        if i not in listToCheck:
            return False
    return True


# Function for removing repeated number from a list
def removeRepeat(listToRemoveFrom):
    listToRemoveFrom.sort()
    for j in range(2):
        for i in range(len(listToRemoveFrom)):
            try:
                if listToRemoveFrom[i] in listToRemoveFrom[i+1::]:
                    listToRemoveFrom.pop(i)
            except IndexError:
                continue

# Creation of the List Comprehension
listComprehension = [i**j for i in range(1,10) for j in range(1,5)]
# Creating a temp list to store the actual list while i change the actual list
tempList = listComprehension.copy()

# Calling both of the function
removeRepeat(listComprehension)
print(checkListInOneAnother(listComprehension, tempList))



