import math


def checking(a, b, c):
    delta = b*b-4*b*c
    if delta > 0:
        root1 = (-b + math.sqrt(delta))/(2*a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("The Roots are REAL and UNEQUAL")
        print("Roots are " + str(root1) + ", " + str(root2))
    elif delta == 0:
        root1 = -b / (2 * a)
        print("The Roots are REAL and EQUAL")
        print("Roots are " + str(root1))
    elif delta < 0:
        root1 = complex((-b)/(2*a), (math.sqrt(-delta)) / (2 * a))
        root2 = complex((-b)/(2*a), (- math.sqrt(-delta)) / (2 * a))
        print("The Roots are IMAGINARY and UNEQUAL")
        print("Roots are " + str(root1) + ", " + str(root2))


if __name__ == '__main__':
    checkingVar = ['Y', 'YES', 'YE']
    dummyVar = 'Y'
    while dummyVar.upper() in checkingVar:
        a = int(input("Please Enter the Coefficient of x squared:- "))
        b = int(input("Please Enter the Coefficient of x :- "))
        c = int(input("Please Enter the Constant:- "))
        checking(a, b, c)
        dummyVar = input("Do You Want To Continue")
