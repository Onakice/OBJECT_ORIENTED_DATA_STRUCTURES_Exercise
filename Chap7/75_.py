class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def append(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._append(self.root, data)
        return self.root

    def _append(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._append(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._append(node.right, data)

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self, data):
        pos = self._checkpos(self.root, data)
        if pos is None:
            print("Not exist")
        else:
            print(pos)

    def _checkpos(self, node, data):
        if node is None:
            return None
        
        if node.data == data:
            if node == self.root:
                return "Root"
            
            elif node.left is None and node.right is None:
                return "Leaf"
            else:
                return "Inner"
        
        elif data < node.data:
            return self._checkpos(node.left, data)
        else:
            return self._checkpos(node.right, data)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.append(inp[i])
T.printTree(root)
T.checkpos(inp[0])