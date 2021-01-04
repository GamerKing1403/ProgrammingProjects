with open("file.txt", "r") as myFile:
    for i in myFile.readlines():
        j = i.split(' ')
        for a in j:
            print(a, '#')
