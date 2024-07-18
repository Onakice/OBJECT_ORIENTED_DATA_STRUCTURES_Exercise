class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def get_node(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            current = current.next
            count += 1
        return None
    
    def set_next(self, index1, index2):
        if self.head is None:
            print(f"Error! {{list is empty}}")
            return
        
        node1 = self.get_node(index1)
        if node1 is None:
            print(f"Error! {{index {index1} not in length}}")
            return
        
        node2 = self.get_node(index2)
        if node2 is None:
            print(f"index not in length, append : {index2}")
            self.append(index2)
            node2 = self.get_node(index2)
        
        node1.next = node2
        print(f"Set node.next complete!, index:value = {index1}:{node1.value} -> {index2}:{node2.value}")
    
    def has_cycle(self):
        if self.head is None:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def print_list(self):
        if self.head is None:
            print("Empty")
            return
        
        current = self.head
        while current:
            if current.next:
                print(f"{current.value}->", end="")
            else:
                print(f"{current.value}")
            current = current.next

# สร้าง linked list
ll = LinkedList()

# รับ input และแยกคำสั่ง
input_commands = input("Enter input : ")
commands = input_commands.split(",")

# ประมวลผลคำสั่ง
for command in commands:
    action, param = command.strip().split()
    if action == "A":
        ll.append(int(param))
    elif action == "S":
        index1, index2 = map(int, param.split(":"))
        ll.set_next(index1, index2)

# แสดงผลลัพธ์ linked list
ll.print_list()

# ตรวจสอบการวนซ้ำ
if ll.has_cycle():
    print("Found Loop")
else:
    print("No Loop")

# แสดงผลลัพธ์ linked list อีกครั้ง
ll.print_list()
