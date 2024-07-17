class Queue():
    def __init__(self):
        self.items_size = 0
        self.items = []

    @property
    def size(self):
        return self.items_size
    
    def deQueue(self):
        if self.items:
            self.items_size -= 1
            return self.items.pop(0)
        return "Empty"
    
    def enQueue(self, val):
        self.items.append(val)
        self.items_size += 1
    
    def isEmpty(self):
        return not self.items
    
    def __str__(self):
        return f"{self.items}"
    
class Cashier:
    def __init__(self, service_time):
        self.service_time = service_time
        self.current_time = 0

    def process_customer(self, current_time):
        if self.current_time <= current_time:
            self.current_time = current_time + self.service_time
            return True
        return False
    

# def simulate_queue(people):
def simulate_queue():
    # main_queue = Queue()
    # cashier1 = Queue()
    # cashier2 = Queue()

    main = input("Enter Input : ")
    main_queue = list(main)

    queue1 = []
    queue2 = []

    cashier1 = Cashier(service_time=3)
    cashier2 = Cashier(service_time=2)

    time = 0

    while main_queue or queue1 or queue2:
        print(f"{time} {main_queue} {cashier1} {cashier2}")

        # ย้ายลูกค้าจาก main_queue ไปยัง queue1 หรือ queue2
        if queue1 and not cashier1.process_customer(time):
            queue1.append(main_queue.pop(0))
        elif queue2 and not cashier2.process_customer(time):
            queue2.append(main_queue.pop(0))
        elif not queue1 and not queue2 and main_queue:
            queue1.append(main_queue.pop(0))
        
        # ประมวลผลลูกค้าใน cashier 1
        if queue1 and cashier1.process_customer(time):
            queue1.pop(0)
        
        # ประมวลผลลูกค้าใน cashier 2
        if queue2 and cashier2.process_customer(time):
            queue2.pop(0)
        
        time += 1

    # for person in people:
    #     main_queue.enQueue(person)

    # time_cashier1 = 0
    # time_cashier2 = 0

    # max_time = len(people) + 1

    # for time in range(max_time):
    #     print(f"{time} {main_queue} {cashier1} {cashier2}")

    #     if time_cashier1 % 3 == 0 and not cashier1.isEmpty():
    #         cashier1.deQueue()

    #     if time_cashier2 % 2 == 0 and not cashier2.isEmpty():
    #         cashier2.deQueue()
        
    #     if not main_queue.isEmpty():
    #         if cashier1.size < 5:
    #             cashier1.enQueue(main_queue.deQueue())
    #         elif cashier2.size < 5:
    #             cashier2.enQueue(main_queue.deQueue())

    #     if main_queue.isEmpty() and time == max_time -1 :
    #         max_time += 1

# inps = input("Enter Input : ")
# inps_list = list(inps)

# simulate_queue(inps_list)

simulate_queue()