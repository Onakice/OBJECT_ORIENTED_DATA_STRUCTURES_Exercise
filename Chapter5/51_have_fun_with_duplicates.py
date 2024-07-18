class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove_duplicates(self):
        current = self.head
        prev = None
        duplicates = set()
        duplicate_count = 0
        while current:
            if current.data in duplicates:
                prev.next = current.next
                duplicate_count += 1
            else:
                duplicates.add(current.data)
                prev = current
            current = current.next
        return duplicate_count

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return ' '.join(result)

def main():

    inps = input("Enter Input : ")
    inps_data = list(map(int, inps.split()))

    linked_list = LinkedList()
    for num in inps_data:
        linked_list.append(num)

    print("Linked list now is", linked_list)
    duplicate_count = linked_list.remove_duplicates()
    print(f"there are {duplicate_count} duplicates that been remove")
    print("Remove duplicates Linked list", linked_list)
    
if __name__ == "__main__":
    main()