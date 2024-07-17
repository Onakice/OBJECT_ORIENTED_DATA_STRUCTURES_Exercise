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
    


inps = input("Enter Input : ")
# inps_list = list(inps)

main_queue = Queue()
cashier1 = Queue()
cashier2 = Queue()

time = 0
time1 = 0
time2 = 0

# print(inps_list)

for inp in inps:
    main_queue.enQueue(inp)

max_time = main_queue.size + 1
print(f"max_time is : {max_time}")

# print(main_queue)

for i in range(main_queue.size):

    if time1 % 3 != 0:
        cashier1.enQueue(main_queue.deQueue())
    elif time1 % 3 == 0:
        cashier1.enQueue(main_queue.deQueue())
        cashier1.deQueue()

    if time != max_time :
        time += 1
        print(f"{time} {main_queue} {cashier1} {cashier2}")

