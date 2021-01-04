with open('nameRollMarks.txt', 'r') as myFile:
    roll, name = [], []
    for lines in myFile.readlines():
        tempRoll, tempFirstName, tempLastName, tempMarks = lines.split(" ")
        roll.append(int(tempRoll))
        name.append(tempFirstName+" "+tempLastName)
    inputRoll = input("Enter The roll number to search for:- ")
    try:
        index = roll.index(int(inputRoll))
    except ValueError:
        index = -1
    if index == -1:
        print("The roll number doesn't Exist")
    else:
        print("The Name At the roll number", inputRoll, 'is', name[index])
