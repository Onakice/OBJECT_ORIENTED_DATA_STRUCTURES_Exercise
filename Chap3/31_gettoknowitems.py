class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(f"Add = {value} and Size = {len(self.stack)}")

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            index = len(self.stack)
            print(f"Pop = {value} and Index = {index}")
        else:
            print(-1)

    def display(self):
        if self.stack:
            print("Value in Stack ="," ".join(map(str, self.stack)))
            pass
        else:
            print("Value in Stack = Empty")

stack = Stack()

commands = input("Enter Input : ").split(',')

for command in commands:
    command = command.strip()
    if command.startswith('A'):
        _, value = command.split()
        stack.push(int(value))
    elif command == 'P':
        stack.pop()

stack.display()