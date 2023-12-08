class BST:

    class Node:

        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data, node = None):
        if self.root is None:
            self.root = self.Node(data)
        else:
            if node is None:
                node = self.root
            if data < node.data:
                if node.left is None:
                    node.left = self.Node(data)
                else:
                    self.insert(data, node.left)
            elif data >= node.data:
                if node.right is None:  
                    node.right = self.Node(data)
                else:
                    self.insert(data, node.right)
 
        
    def nth_smallest(self, n, node=None):
        if node is None:
            node = self.root
        result = self._nth_smallest(n, node)
        if result is not None:
            self.count = 0
            return result.data
        else:
            self.count = 0
            return None

    def _nth_smallest(self, n, node):
        if node is None:
            return None
        left = self._nth_smallest(n, node.left)
        if left is not None:
            return left
        self.count += 1
        if self.count == n:
            return node
        return self._nth_smallest(n, node.right)


tree = BST()

keys = [20, 8, 22, 4, 12, 10, 14, 9]

for key in keys:
    tree.insert(key)

print(tree.nth_smallest(3))