class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def size(self):
        return len(self.items)
    
    def count_visible_trees(self):
        if self.size() == 0:
            return 0
        
        seen_trees = 0  # At least see the last tree Kritda passed
        max_height = float('-inf')  # Start with negative infinity
        
        # Traverse the stack from top to bottom
        for height in reversed(self.items):
            if height > max_height:
                seen_trees += 1
                max_height = height
        
        return seen_trees

# Initialize a stack
S = Stack()

# Example input: A 4,A 3,B
inp = input('Enter Input : ').split(',')

for command in inp:
    command = command.strip()
    if command.startswith('A'):
        _, height = command.split()
        S.push(int(height))
    elif command == 'B':
        visible_trees = S.count_visible_trees()
        print(visible_trees)
