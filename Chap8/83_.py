class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        print("Right Rotation")
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        print("Left Rotation")
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        if not root:
            print(f"insert : {key}")
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            print("Left Left Rotation")
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            print("Right Right Rotation")
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            print("Left Right Rotation")
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            print("Right Left Rotation")
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def print_tree(self, root, level=0, prefix=""):
        if root is not None:
            self.print_tree(root.right, level + 1, "     ")
            print(" " * 5 * level + prefix + str(root.key))
            self.print_tree(root.left, level + 1, "     ")

if __name__ == "__main__":
    avl = AVLTree()
    root = None
    inputs = [int(i) for i in input("Enter Input : ").split()]

    for key in inputs:
        root = avl.insert(root, key)
        avl.print_tree(root)
        print("=" * 20)
