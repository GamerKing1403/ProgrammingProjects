def one():
    def compute(num):
        if(num == 1):
            return 1
        else:
            return(num + compute(num-1))

    # main
    last = 4
    ssum = compute(last)
    print("The Sum of the series from 1 ..",last,"is",ssum)


def two():
    def bp(sg,n):
        if n>0:
            print(sg[n],end='')
            bp(sg,n-1)
        elif n == 0:
            print(sg[0])

    # __main__
    s = input("Enter a String :- ")
    bp(s, len(s)-1)

# def power(a,b):
#     if b==0:
#         return 1
#     else:
#         return a*power(a,b-1)

# # __main__
# print("Enter the positive numbers bellow: ")
# num = int(input("Enter the base number: "))
# p = int(input("raised to the power of: "))
# result = power(num,p)
# print(num,"raised to the power of ",p,"is",result)


#factorial using recursive function

# def factorial(n):
#     if n < 2:
#         return 1
#     return n*factorial(n-1)

# #__main__
# n = int(input("Enter a number(>0): "))
# print("Factorial of",n,"is",factorial(n))

# Practice Session

# tuple1 = ('a','b','c','d','e')
# char = input("Enter a Single Letter Without quotes: ")
# if char in tuple1:
#     count = 0
#     for a in tuple1:
#         if a!= char:
#             count += 1
#         else:
#             break
#     print(char," is at index ",count," in ",tuple1)
# else:
#     print(char,"is Not in ",tuple1)

# write a program to reverse a string and check if it is a pallindrome or not

# string = input("Please Enter the String You want to check :- ")
# if string == string[::-1]:
#     print(string," is a Pallindrome.")
# else:
#     print(string," is not a pallindrome.")

# Insertion Sorting

# alist = [15,2,6,3,2,7,4,5]
# print("Orignal List: ",alist)
# for i in range(1,len(alist)):
#     key = alist[i]
#     j = i-1
#     while j >=0 and key < alist[j]:
#         alist[j+1] = alist[j]
#         j = j-1
#     else:
#         alist[j+1] = key
# print("List after sorting: ",alist)

# Bubble sort

# alist = [15,6,3,4,7,6,9]
# print("orignal List: ",alist)
# n = len(alist)
# for i in range(n):
#     for j in range(n-i-1):
#         if alist[j]>alist[j+1]:
#             alist[j],alist[j+1] = alist[j+1],alist[j]
# print("List After sorting : ",alist)

#
# def arCalc(x,y):
#     return x+y,x-y,x*y,x/y,x%y

# # __main__
# num1 = int(input("Enter the first Number: "))
# num2 = int(input("Enter the Second Number: "))
# add,sub,mult,div,mod = arCalc(num1,num2)
# print("Sum: ",add)
# print("Diffrence: ",sub)
# print("Product: ",mult)
# print("Division: ",div)
# print("Modulo: ",mod)

# Binary Search
# def binSearch(ar,key,low,high):
#     if low > high:
#         return -999
#     mid = int((low+high)/2)

#     if key == ar[mid]:
#         return mid
#     elif key<ar[mid]:
#         high = mid-1
#         return binSearch(ar,key,low,high)
#     else:
#         low = mid + 1
#         return binSearch(ar,key,low,high)

# #__main__
# ary = [12,15,21,25,28,32,33,36,43,45]
# item = int(input("Enter Search Item: "))
# res = binSearch(ary,item,0,len(ary)-1)
# if res >=0:
#     print(item," Found at index ",res)
# else:
#     print("Sorry!",item," Not Found in array.")

# # Factorial
# def factorial(n):
#     if n<2:
#         return 1
#     return n*factorial(n-1)

# #__main__
# n = int(input("Enter the Number(>0):- "))
# print("Factorial of ",n," is ",factorial(n))

# fibonacci series

# def fib(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# #__main__
# n = int(input("Enter The Last term required:- "))
# for i in range(1,n+1):
#     print(fib(i),end=', ')
# print("...")


# def gcd(p,q):
#     if q == 0:
#         return p
#     return gcd(p,p%q)
# #__main__
# print(gcd(1440, 408))


# def sqsum(n):
#     if n == 1:
#         return 1
#     return n*n + sqsum(n-1)
# #__main__
# n = int(input("Enter the Value of n: "))
# print(sqsum(n))


# def linearSearch(arr,element,index=0):

#     if element == arr[index]:
#         return index
#         print(index)
#     elif index < len(arr)-1:
#         return linearSearch(arr,element,index+1)


# #__main__
# arr = list(eval(input("Enter the list seprated by commas:- ")))
# element = int(input("Enter the element to seach for:- "))
# print("The element",element,"is at the index",linearSearch(arr,element))




# check if a number is prime or not using linear approach
# n = int(input("Enter The number:- "))

# prime_flag = 0
# for i in range(2,n):
#     if n%i == 0:
#         prime_flag = 1
#         break

# if prime_flag == 0:
#     print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")


# def linearSearch(arr,x):
#     i = 0
#     n = len(arr)
#     while i<n and x!=arr[i]:
#         i = i+1
#     if i <n:
#         return i 
#     else:
#         return None

# # __main__
# arr = eval(input("Enter the array seperated by commas:- "))
# x = input("Enter the element to search for:- ")
# try:
#     x = int(x)
# except ValueError as e:
#     print("You have entered a string.\n Doing search with the string.")

# print(linearSearch(arr,x))

# def binsearch(ar,key):
#     low = 0 
#     high = len(ar) - 1
#     while low <= high:
#         mid = int((low+high)/2)
#         if key == ar[mid]:
#             return mid
#         elif key<ar[mid]:
#             high = mid -1
#         else:
#             low = mid +1
#     else:
#         return None
# # __main__
# arr = eval(input("Enter the array seperated by commas:- "))
# x = input("Enter the element to search for:- ")
# try:
#     x = int(x)
# except ValueError as e:
#     print("You have entered a string.\n Doing search with the string.")

# print(binsearch(arr,x))