#File Handling

def one():
    myfile = open("C:\\Users\\user\\Documents\\ProgrammingProjects\\VSCodeProjects\\PythonProject\\School\\abc.txt","r")
    s = myfile.read(10)
    print(s, end = ' ')
    s = myfile.readline()
    print(s, end = ' ')
    s = myfile.readline()
    print(s, end = ' ')
    myfile.close()

#Read n bytes and then reading some more byte from the last position read

def two():
    myfile = open("C:\\Users\\user\\Documents\\ProgrammingProjects\\VSCodeProjects\\PythonProject\\School\\abc.txt","r")
    s = myfile.read(10)
    print(s)
    l = myfile.read(20)
    print("---------")
    print(l)
    myfile.close()

#EOC- end of class

# Calculate the total number of bytes in a file
def three():
    myfile = open(r'C:\Users\user\Documents\ProgrammingProjects\VSCodeProjects\PythonProject\School\abc.txt','r')
    total_len = 0
    for l in myfile:
        total_len += len(l)
    print("Number of Bytes in the file is:- "+str(total_len))
    myfile.close()

# Calaulate the number of lines in the file
def four():
    myfile = open(r'C:\Users\user\Documents\ProgrammingProjects\VSCodeProjects\PythonProject\School\abc.txt','r')
    no_line = 0
    for l in myfile:
        no_line += 1
    print("The Number of lines is :-"+str(no_line))
    myfile.close()

# Writing
def five():
    myfile = open(r'C:\Users\user\Documents\ProgrammingProjects\VSCodeProjects\PythonProject\School\abc.txt','w+')
    for i in range(5):
        name = input("Enter the name of the student:- ")
        myfile.write(name)
        myfile.write('\n')
    myfile.close()

#Create a file with some name seperated by /n without using write function
def six():
    myfile = open(r'C:\Users\user\Documents\ProgrammingProjects\VSCodeProjects\PythonProject\School\abc.txt','w')
    lst = []
    for i in range(5):
        name = input("Enter the name of the student:- ")
        lst.append(name+'\n')
    myfile.writelines(lst)
    myfile.close()

# write a program to ge tthe roll no name of the students and store these details in file named marks.txt
def seven():
    count = int(input('How many students are there in the class? '))
    fileout = open('marks.txt','w')
    for i in range(count):
        print("Enter Student Detail ",(i+1),"bellow: ")
        rollno = int(input('Rollno:'))
        name = input('Name: ')
        marks = float(input('Marks: '))
        rec = str(rollno)+","+name+','+str(marks)+'\n'
        fileout.write(rec)
    fileout.close()

# Write a program to add two more student details to the file created above

def eight():
    fileout = open('marks.txt','a')
    for i in range(2):
        print("Enter Student Detail ",(i+1),"bellow: ")
        rollno = int(input('Rollno:'))
        name = input('Name: ')
        marks = float(input('Marks: '))
        rec = str(rollno)+","+name+','+str(marks)+'\n'
        fileout.write(rec)
    fileout.close()


def stats(filename):
    longest = ""
    for line in open(filename):
        if len(line) > len(longest):
            longest = line
    print('Longest line`s length = ',len(longest))
    print(longest)

# stats('abc.txt')
def nine():
    out = open("output.txt","w")
    out.write("Hello World!\n")
    out.write('How Are You?')
    out.close()
    print(open("output.txt","r").read())





