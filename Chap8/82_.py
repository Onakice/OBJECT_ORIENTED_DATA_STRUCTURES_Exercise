class TreeNode(object): 
    def __init__(self, val): 
        self.val = int(val)  # Ensure the values are integers
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)

class AVL_Tree(object): 
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        
        # Insert node into the tree
        if int(key) < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Get the balance factor
        balance = self.getBalance(root)

        # Balance the tree if needed
        # Case 1 - Left Left
        if balance > 1 and int(key) < root.left.val:
            print("Not Balance, Rebalance!")
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and int(key) > root.right.val:
            print("Not Balance, Rebalance!")
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and int(key) > root.left.val:
            print("Not Balance, Rebalance!")
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and int(key) < root.right.val:
            print("Not Balance, Rebalance!")
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :", e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")
