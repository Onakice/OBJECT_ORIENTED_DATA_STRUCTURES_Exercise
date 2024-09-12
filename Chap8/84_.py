from collections import deque

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def print_tree(self):
        levels = []
        self._print_tree(self.root, 0, levels)
        max_width = 2 ** (len(levels) - 1) * 3
        for i, level in enumerate(levels):
            spacing = max_width // (2 ** i)
            line = ""
            for node in level:
                if node is None:
                    line += " " * spacing
                else:
                    line += str(node.key).center(spacing, " ")
            print(line)

    def _print_tree(self, node, depth, levels):
        if node is None:
            if len(levels) <= depth:
                levels.append([None])
            else:
                levels[depth].append(None)
            return
        if len(levels) <= depth:
            levels.append([])
        levels[depth].append(node)
        self._print_tree(node.left, depth + 1, levels)
        self._print_tree(node.right, depth + 1, levels)

    def burn_tree(self, start_key):
        # Find the node to start burning from
        start_node = self._find_node(self.root, start_key)
        if not start_node:
            print(f"There is no {start_key} in the tree.")
            return
        
        burned_nodes = set()
        queue = deque([(start_node, 0)])

        while queue:
            nodes_to_burn = set()
            for _ in range(len(queue)):
                node, minute = queue.popleft()
                if node is None or node.key in burned_nodes:
                    continue

                nodes_to_burn.add(node.key)
                # Enqueue children and parent nodes
                if node.left:
                    queue.append((node.left, minute + 1))
                if node.right:
                    queue.append((node.right, minute + 1))
                parent = self._find_parent(self.root, node)
                if parent:
                    queue.append((parent, minute + 1))

            if nodes_to_burn:
                burned_nodes.update(nodes_to_burn)
                print(f"Minute {minute}: {' '.join(map(str, sorted(nodes_to_burn)))}")

    def _find_node(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._find_node(node.left, key)
        return self._find_node(node.right, key)

    def _find_parent(self, root, child):
        if root is None or root == child:
            return None
        if root.left == child or root.right == child:
            return root
        if child.key < root.key:
            return self._find_parent(root.left, child)
        return self._find_parent(root.right, child)
    
input_data = input("Enter node values and burn node : ")

# แยกข้อมูลและประมวลผล
nodes_str, burn_key_str = input_data.split('/')
nodes = list(map(int, nodes_str.split()))
burn_key = int(burn_key_str)

# สร้างและแทรกค่าใน AVL Tree
avl = AVLTree()
for node in nodes:
    avl.insert(node)

print("Initial Tree:")
avl.print_tree()
print("\nBurning Process:")
avl.burn_tree(burn_key)