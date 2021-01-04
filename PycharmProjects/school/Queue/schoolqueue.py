def cls():
    print('\n'*100)


def isEmpty(qu):
    if not qu:
        return True
    else:
        return False


def Enqueue(qu, newItem):
    global front, rear
    qu.append(newItem)
    if len(qu) == 1:
        front = rear = 0
    else:
        rear = len(qu) - 1


def Dequeue(qu):
    global front, rear
    if isEmpty(qu):
        return "Underflow"
    else:
        deletedItem = qu.pop(0)
    if len(qu) == 0:
        front = rear = None
    return deletedItem


def Peek(qu):
    global front
    if isEmpty(qu):
        return "Underflow"
    else:
        front = 0
    return qu[front]


def Display(qu):
    global front, rear
    if isEmpty(qu):
        print("Queue Empty!!")
    elif len(qu) == 1:
        print(qu[0], "<== front, rear")
    else:
        front = 0
        rear = len(qu) - 1
        print(qu[front], "<- front")
        for a in range(1, rear):
            print(qu[a])
        print(qu[rear], '<- rear')


if __name__ == '__main__':
    queue = [0]
    front = None
    rear = None
    while True:
        cls()
        print("QUEUE OPERATIONS")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display Queue")
        print("5. Exit")
        ch = int(input("Enter your choice(1-5)- "))
        if ch == 1:
            item = int(input("Enter Item: "))
            Enqueue(queue, item)
            input("Press Enter to Continue...")
        elif ch == 2:
            item = Dequeue(queue)
            if item == "Underflow":
                print("Underflow Queue Empty!!")
            else:
                print("Dequeue-ed item is:- ", item)
            input("Press Enter to Continue...")
        elif ch == 3:
            item = Peek(queue)
            if item == "Underflow":
                print("Queue is Empty!!")
            else:
                print("FrontMost Element is", item)
            input("Press Enter to Continue...")
        elif ch == 4:
            Display(queue)
            input("Press Enter to Continue...")
        elif ch == 5:
            break
        else:
            print("Invalid Choice!!")
            input("Press Enter to Continue...")
