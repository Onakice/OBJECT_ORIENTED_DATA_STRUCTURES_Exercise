class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(f"Size of STACK: {len(self.stack)}")

    def pop(self):
        if self.stack:
            value = self.stack.pop()
            index = len(self.stack)
            print(f"Value: {value}, Index: {index}")
        else:
            print(-1)

    def display(self):
        if self.stack:
            print(" ".join(map(str, self.stack)))
        else:
            print("Empty")

# สร้าง Stack
stack = Stack()

# รับคำสั่งจากผู้ใช้
commands = input("Enter Input: ").split(',')

# ประมวลผลคำสั่ง
for command in commands:
    command = command.strip()
    if command.startswith('A'):
        _, value = command.split()
        stack.push(int(value))
    elif command == 'P':
        stack.pop()

# แสดงผลลัพธ์
stack.display()
