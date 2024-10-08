class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def multipleThree(self, node, data):
        if node == None:
            return
        self.multipleThree(node.left, data)
        if int(node.data) > int(data):
            node.data = int(node.data)*3
        self.multipleThree(node.right, data)

T = BST()
inps, k = input("Enter Input : ").split("/")
inpslist = [int(i) for i in inps.split(" ")]
for i in inpslist:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
T.multipleThree(root, k)
T.printTree(root)