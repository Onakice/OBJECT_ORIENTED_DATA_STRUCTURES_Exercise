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

for inp in inps:
    main_queue.enQueue(inp)

max_time = main_queue.size + 1

# for i in range(main_queue.size):
    
#     if time1 % 3 == 0 and time1 != 0:
#         cashier1.enQueue(main_queue.deQueue())
#         cashier1.deQueue()
#         time1 = 0
#         print(f"time1 if   : {time1} i is : {i} q : {cashier1}")
#     elif time1 % 3 == 0:
#         cashier1.enQueue(main_queue.deQueue())
#         time1 += 1
#         print(f"time1 elif : {time1} i is : {i} q : {cashier1}")

#     if time != max_time :
#         time += 1
#     #     print(f"{time} {main_queue} {cashier1} {cashier2}")

while time < max_time:

    # if time1 % 3 == 0 and time1 != 0:
    #     cashier1.deQueue()
    #     time1 = 0
    # if not main_queue.isEmpty():
    #     cashier1.enQueue(main_queue.deQueue())
    # time1 += 1
    # print(f"time1 : {time1}, cashier1 : {cashier1}")

    # if time2 % 2 == 0 and time2 != 0 :
    #     cashier2.deQueue()
    #     time2 = 0
    # if not main_queue.isEmpty():

    if not main_queue.isEmpty():
        if cashier1.size < 5:
            # if time1 % 3 == 0 and time1 != 0:
            if time1 % 3 == 0:
            # if time1 != 0 and time1 % 3 == 0:
                cashier1.deQueue()
                time1 = 0
            if not main_queue.isEmpty():
                cashier1.enQueue(main_queue.deQueue())
            time1 += 1
        # elif cashier2.size < 5 :
        #     if time2 % 2 == 0 and time2 != 0:
        #         cashier2.deQueue()
        #         time2 = 0
        #     if not main_queue.isEmpty():
        #         cashier2.enQueue(main_queue.deQueue())
        #         time2 += 1
    # print(f"{time} {main_queue} {cashier1} {cashier2}")
    print(f"time1 : {time1}, cashier1 : {cashier1}")
    time += 1