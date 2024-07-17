class Queue:
    def __init__(self):
        self.items = []
        self.item_size = 0

    @property
    def size(self):
        return self.item_size
    
    def deQueue(self):
        if self.items:
            self.item_size -= 1
            return self.items.pop(0)
        return "Empty"
    
    def enQueue(self, val):
        self.items.append(val)
        self.item_size += 1

    def isEmpty(self):
        return not self.items

    def __str__(self):
        return str(self.items)

inps = input("Enter people : ")

main_queue = Queue()
cashier1 = Queue()
cashier2 = Queue()

for inp in inps:
    main_queue.enQueue(inp)

time = 0
stamp1 = 0
stamp2 = 0

while not main_queue.isEmpty():

    if ((time - stamp1) % 3) == 0 and not cashier1.isEmpty():
        cashier1.deQueue()
        stamp1 = time

    if ((time - stamp2) % 2) == 0 and not cashier2.isEmpty():
        cashier2.deQueue()
        stamp2 = time

    if cashier1.size < 5:
        cashier1.enQueue(main_queue.deQueue())
    else:
        cashier2.enQueue(main_queue.deQueue())
        if cashier2.size == 1:
            stamp2 = time

    time += 1
    print(time, main_queue, cashier1, cashier2)