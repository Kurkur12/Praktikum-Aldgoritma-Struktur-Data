from binarytree import Node
root = Node('do')
root.left = Node('ni')
root.right = Node('yu')
root.right.left = Node('wah')
root.right.right = Node('sa')
root.right.right.right = Node('tro')
root.right.right.right.left = Node('pu')
print(root)

nim = Node('L')
nim.right = Node(2)
nim.right.right = Node(0)
nim.right.right.right = Node(0)
nim.right.right.right.right = Node(2)
nim.right.right.right.right.right = Node(0)
nim.right.right.right.right.right.right = Node(0)
nim.right.right.right.right.right.right.right = Node(1)
nim.right.right.right.right.right.right.right.right = Node(6)
nim.right.right.right.right.right.right.right.right.right = Node(9)
print(nim)


