from node import Node 
def kunjungi( head ):
    curNode = head
    while curNode is not None :
        print(curNode.data)
        curNode = curNode.next
