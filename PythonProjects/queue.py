def cls():
    print('\n'*100)

def isEmpty(Qu):
    if Qu ==[]:
        return True
    else :
        return False

def Enqueue(Qu, item):
    Qu.append(item)
    if len(Qu) == 1:
        front = rear = 0
    else:
        rear = len(Qu) - 1

def Dequeue(Qu):
    if isEmpt(Qu):
        return "UnderFlow"
    else:
        item = Qu.pop(0)
        if len(Qu)== 0:
            front = rear = None
        return item

def Display(Qu):
    if isEmpty(Qu):
        print("Queue Empty!")
    elif len(Qu) == 1:
        print(Qu[0], "<== front, rear")

    else:
        front = 0
        rear = len(Qu) - 1
        print(Qu[front], "<-front")
        for a in range(1,rear):
            print(Qu[a])
        print(Qu[rear],"<-rear")

#__main__

queue = []
front = None

while True:
    cls()
    print("Queue Operations")
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Display Queue")
    print("4. Exit")
    ch = int(input("Enter Your Choice(1-5):"))
    
