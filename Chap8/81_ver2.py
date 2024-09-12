class AVLTree:

    class AVLNode:

        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a, b)
            return self.height

        def getHeight(self, node):
            return -1 if node is None else node.height

        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self, root=None):
        self.root = root

    def add(self, data):
        self.root = self._add(self.root, int(data))
        
    def _add(self, root, data):
        if root is None:
            return AVLTree.AVLNode(data)
        
        if data < root.data:
            root.left = self._add(root.left, data)
        else:
            root.right = self._add(root.right, data)

        root = self._balance(root)
        return root

    def _balance(self, node):
        if node.balanceValue() > 1:
            if node.right and node.right.balanceValue() < 0:
                node.right = self.rotateRightChild(node.right)
            node = self.rotateLeftChild(node)
        elif node.balanceValue() < -1:
            if node.left and node.left.balanceValue() > 0:
                node.left = self.rotateLeftChild(node.left)
            node = self.rotateRightChild(node)
        node.setHeight()
        return node

    def rotateLeftChild(self, root):
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def rotateRightChild(self, root):
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def postOrder(self):
        result = []
        self._postOrder(self.root, result)
        print("AVLTree post-order : " + " ".join(map(str, result)))

    def _postOrder(self, node, result):
        if node is not None:
            self._postOrder(node.left, result)
            self._postOrder(node.right, result)
            result.append(node.data)

    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    @staticmethod
    def _printTree(node, level=0):
        if node is not None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

avl1 = AVLTree()

inp = input('Enter Input : ').split(',')

for i in inp:
    if i[:2] == "AD":
        avl1.add(i[3:])
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        avl1.postOrder()
