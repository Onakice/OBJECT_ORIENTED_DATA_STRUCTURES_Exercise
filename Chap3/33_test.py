class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(infix):
    stack = Stack()
    postfix = []
    for char in infix:
        if char.isdigit() or char.isalpha():
            postfix.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while not stack.isEmpty() and precedence(stack.peek()) >= precedence(char):
                postfix.append(stack.pop())
            stack.push(char)
    
    while not stack.isEmpty():
        postfix.append(stack.pop())
    
    return ''.join(postfix)

inp = input('Enter Infix : ')
postfix = infix_to_postfix(inp)
print('Postfix :', postfix)