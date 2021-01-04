# Just Creating a Stack Class
class Stack:

    def __init__(self):
        self.stack = []
        self.top = None

    def isEmpty(self):
        if self.stack:
            return True
        else:
            return False

    def Push(self, item):
        self.stack.append(item)
        self.top = len(self.stack) - 1

    def Pop(self):
        if self.isEmpty():
            return "Underflow"
        else:
            item = self.stack.pop()
            if len(self.stack) == 0:
                self.top = None
            else:
                self.top = len(self.stack) - 1
            return item

    def Peek(self):
        if self.isEmpty():
            return "Underflow"
        else:
            self.top = len(self.stack) - 1
            return self.stack[self.top]

    def Display(self):
        if self.isEmpty():
            print("Stack empty")
        else:
            self.top = len(self.stack) - 1
            print(self.stack[self.top], "<-top")
            for a in range(self.top - 1, -1, -1):
                print(self.stack[a])
