    def preorder(self, node, stop):
        if node is not None:
            print(ord(node.data), end=' ')
            self.preorder(node.left, stop)
            self.preorder(node.right, stop)

    def inorder(self, node, stop):
        if node is not None:
            self.inorder(node.left, stop)
            print(ord(node.data), end=' ')
            self.inorder(node.right, stop)

    def postorder(self, node, stop):
        if node is not None:
            self.postorder(node.left, stop)
            self.postorder(node.right, stop)
            print(ord(node.data), end=' ')