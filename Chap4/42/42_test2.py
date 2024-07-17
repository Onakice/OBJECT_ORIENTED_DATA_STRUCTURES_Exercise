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

def simulate_queue(people):
    main_queue = Queue()
    cashier1 = Queue()
    cashier2 = Queue()
    
    for person in people:
        main_queue.enQueue(person)
    
    # Calculate the maximum number of iterations
    total_time = len(people) + 1  # Number of people plus one extra minute

    for time in range(total_time):
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

people = list("Lorem_Ipsum")
simulate_queue(people)