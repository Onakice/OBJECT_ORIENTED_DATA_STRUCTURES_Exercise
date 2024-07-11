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

inp = input('Enter Infix : ')
S = Stack()
output = []

for char in inp:
    if char.isalnum():  # check if character is alphanumeric (operand)
        output.append(char)
    elif char == '(':
        S.push(char)
    elif char == ')':
        while not S.isEmpty() and S.peek() != '(':
            output.append(S.pop())
        S.pop()  # pop the '(' from stack
    else:  # operator
        while not S.isEmpty() and precedence(S.peek()) >= precedence(char):
            output.append(S.pop())
        S.push(char)

while not S.isEmpty():
    output.append(S.pop())

print('Postfix :', ''.join(output))
