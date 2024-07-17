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

    time = 0
    cashier1_busy_until = 0
    cashier2_busy_until = 0

    while not (main_queue.isEmpty() and cashier1.isEmpty() and cashier2.isEmpty()):
        print(f"{time} {main_queue} {cashier1} {cashier2}")

        # Process customers in cashier 1
        if time >= cashier1_busy_until and not cashier1.isEmpty():
            cashier1.deQueue()
            cashier1_busy_until = time + 3  # Update when cashier 1 will be free

        # Process customers in cashier 2
        if time >= cashier2_busy_until and not cashier2.isEmpty():
            cashier2.deQueue()
            cashier2_busy_until = time + 2  # Update when cashier 2 will be free

        # Move customers from main queue to available cashier queue
        if not main_queue.isEmpty():
            if cashier1.size < 5 and time >= cashier1_busy_until:
                cashier1.enQueue(main_queue.deQueue())
            elif cashier2.size < 5 and time >= cashier2_busy_until:
                cashier2.enQueue(main_queue.deQueue())
        
        time += 1

    print(f"Simulation complete. Time taken: {time} minutes")

# รับข้อมูลจากผู้ใช้
inps = input("Enter Input : ")
# inps_list = list(map(int, inps.split(',')))
inps_list = list(inps)

simulate_queue(inps_list)
