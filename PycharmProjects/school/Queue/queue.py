class Queue:

    def __init__(self):
        self.qu = []

    def cls(self):
        print('\n' * 100)

    def isEmpty(self):
        if self.qu == []:
            return True
        else:
            return False

    def Enqueue(self, item):
        self.qu.append(item)
        if len(self.qu) == 1:
            front = rear = 0
        else:
            rear = len(self.qu) - 1

    def Dequeue(self):
        if self.isEmpty():
            return "Underflow"
        else:
            item = self.qu.pop(0)
        if len(self.qu) == 0:
            front = rear = None
        return item

    def Peek(self):
        if self.isEmpty():
            return "Underflow"
        else:
            front = 0
        return self.qu[front]

    def Display(self):
        if self.isEmpty():
            print("Queue Empty!!")
        elif len(self.qu) == 1:
            print(self.qu[0], "<== front, rear")
        else:
            front = 0
            rear = len(self.qu) - 1
            print(self.qu[front], "<- front")
            for a in range(1, rear):
                print(self.qu[a])
            print(self.qu[rear], '<- rear')
