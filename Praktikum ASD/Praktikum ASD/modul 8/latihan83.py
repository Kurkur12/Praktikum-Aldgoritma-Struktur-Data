class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty()
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty()
        return self.items.pop()

    def push(self, data):
        self.items.append(data)

class StackLL:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.top is None

    def __len__(self):
        return self.size
    
    def peek(self):
        assert not self.isEmpty()
        return self.top.item

    def pop(self):
        assert not self.isEmpty()
        node = self.top
        self.top = self.top.next
        self.size -= 1
        return node.item

    def push(self):
        self.top = _StackNode(data, self.top)
        self.size += 1

class _StackNode:
    def __init__(self, data, link):
        self.item = data
        self.next = link

##PROMPT = "Masukkan bilangan positif (<0 untuk mengakhiri) : "
##myStack = Stack()
##value = int(input(PROMPT))
##while value >= 0:
##    myStack.push(value)
##    value = int(input(PROMPT))
##while not myStack.isEmpty():
##    value = myStack.pop()
##    print(value)
9