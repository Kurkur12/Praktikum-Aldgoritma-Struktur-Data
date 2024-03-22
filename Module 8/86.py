class Queue(object):
    def __init__(self):
        self.qlist = []
    
    def isEmpty(self):
        return len(self) == 0
    
    def __len__(self):
        return len(self.qlist)
    
    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist.pop(0)

Q = Queue()
Q.enqueue(28)
Q.enqueue(19)
Q.enqueue(45)
Q.enqueue(13)
Q.enqueue(7)
print(Q.qlist)
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
print(Q.qlist)
Q.enqueue(98)
Q.enqueue(54)
Q.dequeue()
print(Q.qlist)
