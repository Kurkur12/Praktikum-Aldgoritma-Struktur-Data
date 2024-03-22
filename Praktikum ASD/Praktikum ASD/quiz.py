import re
import binarytree
##No1
print("No1")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
    if(re.fullmatch(regex, email)):
        print("True")
    else:
        print("False")

if __name__=='__main__':
    email = "doni@student.ums.ac.id"
    check(email)

    email = "doni@ums.ac.id"
    check(email)

    email = "hhsdhfh.com"
    check(email)

##No2
print("")
print("No2")
def check(email):
    if re.match('^[a-zA-Z]+@(?:[a-zA-Z]+\.)?ums\.ac\.id$', email):
        print("True")
    else:
        print("False")

if __name__=='__main__':
    email = "doni@student.ums.ac.id"
    check(email)

    email = "doni@uns.ac.id"
    check(email)

    email = "hhsdhfh@ums.com"
    check(email)


##No3
print("")
print("No3")
from binarytree import Node

root = Node(1)
root.left = Node(2)
root.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(5)
root.right.right.right = Node(8)
root.right.right.right.left = Node(6)
root.right.right.right.right = Node(10)
print(root)



