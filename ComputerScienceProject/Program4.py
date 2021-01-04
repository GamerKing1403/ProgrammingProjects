with open('nameRollMarks.txt', 'r') as myFile:
    roll, name, marks = [], [], []
    wholeFile = myFile.readlines()
    for lines in wholeFile:
        tempRoll, tempFirstName, tempLastName, tempMarks = lines.split(" ")
        roll.append(int(tempRoll))
        name.append(tempFirstName + " " + tempLastName)
        marks.append(int(tempMarks))
    inputRoll = input("Enter The roll number you want to update the marks of:- ")
    newMarks = input("Enter the New Marks:- ")
    try:
        index = roll.index(int(inputRoll))
    except ValueError:
        index = -1
    if index == -1:
        print("The roll number doesn't Exist")
    else:
        with open('nameRollMarks.txt', 'w') as myFile2:
            wholeFile[index] = str(roll[index]) + " " + name[index] + " " + newMarks + "\n"
            myFile2.writelines(wholeFile)
        print("The Marks of the roll", inputRoll, "has been updated.")
