# Program make a simple calculator
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This function adds two numbers
    def add(self):
        return self.x + self.y

    # This function subtracts two numbers
    def subtract(self):
        return self.x - self.y

    # This function multiplies two numbers
    def multiply(self):
        return self.x * self.y

    # This function divides two numbers
    def divide(self):
        return self.x / self.y


if __name__ == '__main__':
    continuingVar = 'Y'
    checking = ['Y', 'YES', 'YE']
    while continuingVar.upper() in checking:
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        # Take input from the user
        choice = input("Enter choice(1/2/3/4): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        Calculator1 = Calculator(num1, num2)

        if choice == '1':
            print(num1, "+", num2, "=", Calculator1.add())
        elif choice == '2':
            print(num1, "-", num2, "=", Calculator1.subtract())
        elif choice == '3':
            print(num1, "*", num2, "=", Calculator1.multiply())
        elif choice == '4':
            print(num1, "/", num2, "=", Calculator1.divide())
        else:
            print("Invalid input")
        num2 = 0
        num1 = 0
        continuingVar = input("Do You Want To Continue? ")
