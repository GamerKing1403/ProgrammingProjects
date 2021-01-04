# Importing my File Created With a class named Stack
from Stack.stack import Stack
# Main Function.
if __name__ == "__main__":
    # Creating a Stack Object
    stack = Stack()
    # Going into a While loop till user tells to stop
    while True:
        # Printing out all the Operations
        print("STACK OPERATIONS")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display Stack")
        print("5. Exit")
        # Taking the Choice
        ch = int(input("Enter Your Choice(1-5): "))
        # Creating A switch statement in python
        if ch == 1:
            # Taking the item to push
            item = int(input("Enter item: "))
            # Pushing the item
            stack.Push(item)
        elif ch == 2:
            # Poping an item
            item = stack.Pop()
            # checking for Underflow
            if item == "Underflow":
                print("Underflow, stack is Empty!!")
            else:
                print("Popped item is", item)
        elif ch == 3:
            # peeking for the top value
            item = stack.Peek()
            # checking for Underflow
            if item == "Underflow":
                print("Underflow, The Stack is Empty!!")
            else:
                print("Topmost Item is, ", item)
        elif ch == 4:
            # Displaying the Stack
            stack.Display()
        elif ch == 5:
            # Breaking Out of the loop
            break
        else:
            # Fail safe for when the user pressing wrong keys
            print("Invalid choice!")
