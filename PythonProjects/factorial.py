
# Geting the Value from the user
x = int(input("Enter The Factorial you want:-"))

# Setting the initial value of factorial to be 1
factorial = 1

# Looping through all the values from 1 to the value given and Multiply the value to the factorial variable
for i in range(1,x+1):
    factorial *= i

# Printing Out the Factorial Value
print("The Factorial of", x ,"is:-", factorial)
