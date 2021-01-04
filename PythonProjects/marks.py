num = int(input("Enter the Number of students:- "))
for i in range(num):
    roll = int(input("Enter the roll number:- "))
    name = input("Enter the Name:- ")
    marks = int(input("Enter the Marks:- "))
    file = open("marks.txt",'a+')
    file.write("Name: "+name+" Roll: "+str(roll)+" Marks: "+str(marks))
    file.close()
    
