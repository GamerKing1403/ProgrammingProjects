# n = int(input("Please Enter the Number:-"))
#
# def factorial(n):
#     factorial_of_n = 1
#     for i in range(1,n+1):
#         factorial_of_n *= i
#     return factorial_of_n
# #print(factorial(n))
# def factorial(n,a):
#     pass
#
#
# def factorial_anotherway():
#     pass
#
# if __name__ == "__main__":
#     print(0.001 + 0.002)
# def q1():
#     # Take any 5 numbers and arrange them in ascending order.
#     ls = []
#     for i in range(5):
#         ls[i] = int(input("Enter The "+str(i+1)+"th Number"))
#     ls = ls.sort()
#     print(ls)
# # Write a userdefined fuction in which calculate the sum of n natural numbers, claculate the sum of squares of n natural num and cubes.
# def sumOfNNumber(n):
#     nNatural  = 0
#     sqNatural = 0
#     cubeNatural = 0
#     for i in range(1,n+1):
#         nNatural += i
#         sqNatural += i **2
#         cubeNatural += i ** 3
#     return nNatural, sqNatural, cubeNatural
# n = int(input("Please Enter the value of n:- "))
# sumOfN,sumOfSq,sumOfCube = sumOfNNumber(n)
# print('The Sum of N natural Number = '+str(sumOfN))
# print('The Sum of sq of N natural Number = '+str(sumOfSq))
# print('The Sum of cube of N natural Number = '+str(sumOfCube))

# Write a program that checks for presence of a value and print its key
# val = int(input("Enter the value to check:- "))
# reqDic = dict()
# data = input('Enter the keys and values seperated by ":" ')
# temp = data.split(':')
# for i in range(int(len(temp)/2)+1):
#     reqDic[temp[i]] = int(temp[i+1])
#
# print(reqDic)
# for value,key in reqDic.items():
#     if value == val:
#         print("FOUND at "+str(key))
#     else:
#         print("NOT FOUND in the provided list")

# a bar chart is drawn to represent sales data of various models of cars for a month write appropriate statments in python to provide labels month june and sale done to x and y axis respectively
# write to create a pi chart for sequence pawn = [23.4, 17.8, 25, 34, 40] for zones east west north south central show north zones value exploded show percentage contribution for each zone the pi chart should be circular


import numpy as np
import matplotlib.pyplot as pl

# models = ['Car a', 'Car b','Car c']
# sales = [100, 200, 150]
# x = np.arange(3)
# pl.bar(x,sales)
# pl.xticks(x, models)
# pl.xlabel("Car Models")
# pl.ylabel("Sales(In Thousands)")
# pl.show()



# con = [23.4, 17.8 , 25, 34, 48]
# zones = ["East", 'West', 'North', 'South', 'Central']
# pl.axis("equal")
# pl.pie(con,labels=zones,explode=[0,0,0.2,0,0],autopct="%1.2f%%")
# pl.show()

# zones = ["North",'South','East', 'West','Central']
# rainfall = {'Jan':[140,160,140,180,110],'Feb':[130,200,180,150,160],'Mar':[130,130,150,200,130],'Apr':[190,200,170, 140,140,170],'May':[160, 200, 190, 180, 120],'Jun':[200, 170, 140,140,170],'Jul':[]}

#check whether a number is pallindrome or not and print the reverse of a number
# def NumberPalindrome(number):
#     if number == number[::-1]:
#         print(number +" is A Palindrome...."+number[::-1])
#     else:
#         print(number+" is not A Palindrome..."+number[::-1])
#
#
# number = input("Enter the number you want to check:- ")
# NumberPalindrome(number)

# 3 userdefined function which claculates the sum of n natural numbers squares of sums of n natural numbers and cubes of sum of n natural numbers
# def sumOfN(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     return sum
# 
# def sumOfSq(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i ** 2
#     return sum
# 
# def sumOfCube(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i ** 3
#     return sum
# 
# 
# n = int(input("Please Enter the Number till which you want the sum to be:- "))
# print("The Sum of "+str(n)+" Natural Number is "+str(sumOfN(n)))
# print("The Sum of Squares of "+str(n)+" Natural Number is "+str(sumOfSq(n)))
# print("The Sum of Cubes of "+str(n)+" Natural Number is "+str(sumOfCube(n)))

# check wheather a number is prime or not
#
# def checkPrime(n):
#     i = [2,3,5,7,11]
#     primeOrNot = False
#     for j in i:
#         if n%j != 0 and n != j:
#             primeOrNot  = True
#         else:
#             primeOrNot = False
#             break
#
#     if primeOrNot:
#         print(str(n)+" is Prime.")
#     else:
#         print(str(n)+" is Not Prime.")
#
# n = int(input("Enter the Number to check:- "))
# checkPrime(n)

# finding the fibonacci series using function

# def fibonacciSeries(n):
#     fis,sec = 0, 1
#     print(str(fis)+","+str(sec)+",",end="")
#     for i in range(n):
#         temp = fis+sec
#         fis,sec = sec,temp
#         if i != n-1:
#             print(sec,end=",")
#         else:
#             print(sec)
#
# n = int(input("Enter the number till which you want the Fibonacci Series to be:- "))
# fibonacciSeries(n)









