class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SnakeLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def pop(self, index):
        if index == 0 :
            a = self.head.data
            self.head = self.head.next
            return a
        else:
            t = self.head
            i = 0
            while i<index-1:
                t = t.next
                i = i+1
            a = t.next.data
            t.next = t.next.next
            return a

    def print_list(self):
        snake = []
        current_node = self.head
        while current_node:
            snake.append(current_node.data)
            current_node = current_node.next
        return snake
    
    def formatted_print(self):
        if not self.head:
            return "Empty"
        current_node = self.head
        formatted_snake = [f"({current_node.data})"]
        current_node = current_node.next
        while current_node:
            formatted_snake.append(f"{current_node.data}")
            current_node = current_node.next
        return "->".join(formatted_snake)
    
    def swap(self):
        if not self.head or not self.head.next:
            return
        current = self.head.next
        while current and current.next:
            current.data, current.next.data = current.next.data, current.data
            current = current.next.next
    
    def shake(self):
        prev = None
        current = self.head
        removed_snakes = []
        while current:
            if current.data > self.head.data:
                removed_snakes.append(current.data)
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return removed_snakes

    def fly(self, new_weight):
        self.append(new_weight)

    def divide(self, dad_weight):
        # คำนวณค่าน้ำหนักรวม
        total_weight = 0
        current = self.head
        while current:
            total_weight += current.data
            current = current.next

        # ถ้าค่าน้ำหนักรวมมากกว่าหรือเท่ากับ dad_weight ให้ไม่ทำอะไร
        if total_weight >= dad_weight:
            return []
        
        removed_snakes = []

        # while total_weight < dad_weight and self.head:
        #     popped_data = self.pop()
        #     if popped_data is not None:
        #         removed_snakes.append(popped_data)
        #         total_weight -= popped_data
        #         if popped_data % dad_weight == 0:
        #             # total_weight += popped_data
        #             break

        while total_weight < dad_weight and self.head:
            # หา index ของ node สุดท้าย
            index = 0
            temp = self.head
            while temp.next:
                temp = temp.next
                index += 1
            
            popped_data = self.pop(index)
            if popped_data is not None:
                removed_snakes.append(popped_data)
                total_weight -= popped_data
                if popped_data % dad_weight == 0:
                    break

        return removed_snakes
    
    def swap_head_tail(self):
        if not self.head or not self.head.next:
            return
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
        current.next = self.head.next
        prev.next = self.head
        self.head.next = None
        self.head = current

input_data = input("Snake family: ").strip()
# snake_input, commands_input = input_data.split('/')
try:
    snake_input, commands_input = input_data.split('/')
except ValueError:
    print("Error: Invalid input format. Ensure you have '/' to separate snake weights and commands.")
    exit()

# snake_weights = list(map(int, snake_input.strip().split()))
try:
    snake_weights = list(map(int, snake_input.strip().split()))
except ValueError:
    print("Error: Invalid snake weights format. Ensure all snake weights are integers.")
    exit()

commands = [cmd.strip() for cmd in commands_input.strip().split(',')]

snake = SnakeLinkedList()
for weight in snake_weights:
    snake.append(weight)

print(f"{snake.formatted_print()}")

for command in commands:
    if command.startswith("D"):
        dad_weight = int(command.split()[1])
        removed_snakes = snake.divide(dad_weight)
        print(f"Play success!->{removed_snakes}")
    elif command == "SH":
        removed_snakes = snake.shake()
        print(f"Shake success!->{removed_snakes}")
    elif command == "SW":
        snake.swap()
        print("Swap success!")
        snake.print_list()
    elif command.startswith("F"):
        new_weight = int(command.split()[1])
        snake.fly(new_weight)
        print(f"Steal success!->{new_weight}")
    print(snake.formatted_print())
    print("------------------------------")

print(f"Snake Game : ")