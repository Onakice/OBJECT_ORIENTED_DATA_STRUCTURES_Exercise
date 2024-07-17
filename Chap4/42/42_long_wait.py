class Queue():
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
    
def simulate_queue(people):
    main_queue = Queue()
    cashier1 = Queue()
    cashier2 = Queue()

    for person in people:
        main_queue.enQueue(person)

    time = 0

    # while not main_queue.isEmpty() or not cashier1.isEmpty() or not cashier2.isEmpty():
    while not main_queue.isEmpty():
        print(f"{time} {main_queue} {cashier1} {cashier2}")

        if time % 3 == 0 and not cashier1.isEmpty():
            cashier1.deQueue()

        if time % 2 == 0 and not cashier2.isEmpty():
            cashier2.deQueue()

        if not main_queue.isEmpty():
            if cashier1.size < 5:
                cashier1.enQueue(main_queue.deQueue())
            elif cashier2.size < 5:
                cashier2.enQueue(main_queue.deQueue())

        time += 1

inps = input("Enter Input : ")
inps_list = list(inps)

simulate_queue(inps_list)