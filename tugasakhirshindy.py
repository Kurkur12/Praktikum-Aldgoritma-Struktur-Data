class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def inorder_traversal(self):
        if self.root is None:
            return []
        else:
            return self._inorder_recursive(self.root)

    def _inorder_recursive(self, current_node):
        result = []
        if current_node.left:
            result += self._inorder_recursive(current_node.left)
        result.append(current_node.value)
        if current_node.right:
            result += self._inorder_recursive(current_node.right)
        return result

    def preorder_traversal(self):
        if self.root is None:
            return []
        else:
            return self._preorder_recursive(self.root)

    def _preorder_recursive(self, current_node):
        result = []
        result.append(current_node.value)
        if current_node.left:
            result += self._preorder_recursive(current_node.left)
        if current_node.right:
            result += self._preorder_recursive(current_node.right)
        return result

    def postorder_traversal(self):
        if self.root is None:
            return []
        else:
            return self._postorder_recursive(self.root)

    def _postorder_recursive(self, current_node):
        result = []
        if current_node.left:
            result += self._postorder_recursive(current_node.left)
        if current_node.right:
            result += self._postorder_recursive(current_node.right)
        result.append(current_node.value)
        return result

# Contoh penggunaan program

tree = BinaryTree()

# Membangun pohon biner dengan nilai-nilai node yang diberikan
tree.insert(4)
tree.insert(8)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(5)
tree.insert(7)

# Melakukan penjelajahan inorder
print("Inorder Traversal:")
inorder_result = tree.inorder_traversal()
print(inorder_result)

# Melakukan penjelajahan preorder
print("Preorder Traversal:")
preorder_result = tree.preorder_traversal()
print(preorder_result)

# Melakukan penjelajahan postorder
print("Postorder Traversal:")
postorder_result = tree.postorder_traversal()
print(postorder_result)
