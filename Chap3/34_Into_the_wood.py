class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def size(self):
        return len(self.items)
    
    def seeking(self):
        if self.size() == 0:
            # return "No Trees"
            return 0

        seen_trees = 0
        max_height = float('-inf')

        for height in reversed(self.items):
            if height > max_height:
                seen_trees += 1
                max_height = height

        return seen_trees


        # max_height = self.items[-1]

        # for i in range(self.size() - 2, -1, -1):
        #     if self.items[i] > max_height:
        #         seen_trees += 1
        #         max_height = self.items[i]

        # return print(seen_trees)

S = Stack()

inps = input('Enter Input : ').split(',')

for inp in inps :
    inp = inp.strip()
    if inp.startswith('A'):
        del_head, value = inp.split()
        S.push(int(value))
    elif inp == 'B':
        visible_trees = S.seeking()
        print(visible_trees)