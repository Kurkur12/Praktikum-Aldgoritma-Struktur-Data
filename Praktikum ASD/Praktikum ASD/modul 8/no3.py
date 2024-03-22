#DoniWahyuSaputro
#L200200169

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty(), "Tidka bisa diintip. Stack kosong"
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty(), "Tidka bisa dipop dari Stack kosong"
        return self.items.pop()

    def push(self, data):
        self.items.append(data)

nilai = Stack()
for i in range (16):
    if i%3 == 0:
        nilai.push(i)
    elif i%4 == 0:
        nilai.pop()
print(nilai.items)
