class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Rotation
        if balance > 1 and key < root.left.key:
            # print("Left Left Rotation")
            print("Right Right Rotation")
            return self.right_rotate(root)

        # Right Right Rotation
        if balance < -1 and key > root.right.key:
            # print("Right Right Rotation")
            print("Left Left Rotation")
            return self.left_rotate(root)

        # Left Right Rotation
        if balance > 1 and key > root.left.key:
            print("Left Right Rotation")
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Rotation
        if balance < -1 and key < root.right.key:
            print("Right Left Rotation")
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node.key)
            self.print_tree(node.left, level + 1)

# ตัวอย่างการใช้งาน
tree = AVL_Tree()
root = None

print(" *** AVL Tree Insert Element *** ")
inputs = list(map(int, input("Enter Input : ").split()))

for key in inputs:
    print(f"insert : {key}")
    root = tree.insert(root, key)
    tree.print_tree(root)
    print("====================")
