class Stack():
    def __init__(self, n):
        self.stack = []
        self.size = n
    def push(self, value):
        if len(self.stack) >= self.size:
            print("Stack Full")
        else:
            self.stack.append(value)
    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop(-1)
        else:
            print("Stack Empty")
    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            print("Stack Empty")
    def sortStack(self, sort):
        temp = []
        while sort:
            x = sort.pop()
            while len(temp) > 0:
                if temp[-1] > x:
                    sort.push(temp.pop())
            temp.append(x)
        while temp:
            sort.push(temp.pop())
    def display(self):
        print(self.stack)
    def length(self):
        return len(self.stack)
    def clear(self):
        self.stack = []

stack = Stack(5)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(7)
print(stack.length())
# stack.display()
# stack.pop()
# stack.display()
# stack.clear()
# stack.display()

stack.sortStack(stack)
stack.display()

