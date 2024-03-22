class PriorityQueue(object):

    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)
    
    def isEmpty(self):
        return len(self) == 0
    
    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)
    
    def dequeue(self):
        pass


class _PriorityQEntry(object):
    
    def __init__(self, data, priority):
         self.item = data
         self.priority = priority
    def __str__(self):
        return 'Item: {}\nPriority: {}'.format(self.item, self.priority)

S = PriorityQueue()
S.enqueue('Jeruk', 4)
S.enqueue('Tomat', 2)
S.enqueue('Mangga', 0)
S.enqueue('Duku', 5)
S.enqueue('Papaya', 2)
for i in S.qlist:
    print(i)
S.dequeue()
S.dequeue()
S.dequeue()
for i in S.qlist:
    print(i)
