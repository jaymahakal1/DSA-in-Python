class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def CreateTree(self):
        # pass
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)

    def PreOrderTraversal(self, node):
        if node == None:
            return
        print(node.data, ' ')
        self.PreOrderTraversal(node.left)
        self.PreOrderTraversal(node.right)

    def PostOrderTraversal(self, node):
        if node == None:
            return
        self.PostOrderTraversal(node.left)
        self.PostOrderTraversal(node.right)
        print(node.data, ' ')

    def InorderTraversal(self, node):
        if node == None:
            return
        self.InorderTraversal(node.left)
        print(node.data, ' ')
        self.InorderTraversal(node.right)

    def height(self, node):
        if node == None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
        
    
    
root = BinaryTree()
root.CreateTree()
# root.PreOrderTraversal(root.root)
# print('')
# root.InorderTraversal(root.root)
# print('')
# root.PostOrderTraversal(root.root)
print(root.height(root.root))