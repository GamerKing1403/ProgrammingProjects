newFile = []
with open('file2.txt', 'r') as myFile:
    for line in myFile.readlines():
        if 'a' in line.lower():
            newFile.append(line)

with open('file3.txt', 'w') as myFile:
    myFile.writelines(newFile)
