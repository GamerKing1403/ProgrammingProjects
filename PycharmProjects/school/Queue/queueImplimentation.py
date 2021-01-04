from Queue.queue import Queue

if __name__ == '__main__':

    queue = Queue()
    front = None
    while True:

        queue.cls()
        print("QUEUE OPERATIONS")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display Queue")
        print("5. Exit")
        ch = int(input("Enter your choice(1-5)- "))
        if ch == 1:
            item = int(input("Enter Item: "))
            queue.Enqueue(item)
            input("Press Enter to Continue...")
        elif ch == 2:
            item = queue.Dequeue()
            if item == "Underflow":
                print("Underflow Queue Empty!!")
            else:
                print("Dequeue-ed item is:- ",item)
            input("Press Enter to Continue...")
        elif ch == 3:
            item = queue.Peek()
            if item == "Underflow":
                print("Queue is Empty!!")
            else:
                print("FrontMost Element is", item)
            input("Press Enter to Continue...")
        elif ch == 4:
            queue.Display()
            input("Press Enter to Continue...")
        elif ch == 5:
            break
        else:
            print("Invalid Choice!!")
            input("Press Enter to Continue...")
