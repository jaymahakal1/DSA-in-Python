class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val, node):
        if node == None:
            return Node(val)
        
        if node.val > val:
            node.left = self.insert(val, node.left)
        else:
            node.right = self.insert(val, node.right)

        return node
    
    def search(self, val, node):
        if node == None or node.val == val:
            return node
        
        if node.val > val:
            return self.search(val, node.left)
        else:
            return self.search(val, node.right)

    def inorder(self, node):
        if node == None:
            return
        
        self.inorder(node.left)
        print(node.val, ' ', end='')
        self.inorder(node.right)

    def MinValueNode(self, node):
        p = node
        if p is None:
            return p
        while p.left != None:
            p = p.left
        return p
    
    def delete(self, val, node):
        if node is None:
            return node
        
        if node.val > val:
            node.left = self.delete(val, node.left)
        elif node.val < val:
            node.right = self.delete(val, node.right)
        else:
            if node.left is None and node.right is None:
                return None
            
            if node.left is None:
                tmp = node.right
                del node
                return tmp

            if node.right is None:
                tmp = node.left
                del node
                return tmp
            
            tmp = self.MinValueNode(node.right)
            node.val = tmp.val
            node.right = self.delete(tmp.val, node.right)
        return node



