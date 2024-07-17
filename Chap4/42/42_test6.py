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

# เพิ่มข้อมูลเข้า main_queue
for inp in inps:
    main_queue.enQueue(inp)

time = 0
time1 = 0
time2 = 0

# เริ่มจำลองการทำงานของคิวและแคชเชียร์
while not main_queue.isEmpty():
    # ตรวจสอบแคชเชียร์คนที่ 1
    if not cashier1.isEmpty():
        if time1 != 0 and time1 % 2 == 0:
            cashier1.deQueue()
            time1 = 0

        # เพิ่มเวลาเฉพาะเมื่อแคชเชียร์ 1 ไม่ว่างเปล่า
        time1 += 1

    if not main_queue.isEmpty() and cashier1.size < 5:
        cashier1.enQueue(main_queue.deQueue())

    # ตรวจสอบแคชเชียร์คนที่ 2 เฉพาะเมื่อแคชเชียร์ 1 เต็มแล้ว
    if cashier1.size >= 5:
        if not cashier2.isEmpty():
            if time2 != 0 and time2 % 1 == 0:
                cashier2.deQueue()
                time2 = 0

            # เพิ่มเวลาเฉพาะเมื่อแคชเชียร์ 2 ไม่ว่างเปล่า
            time2 += 1

        if not main_queue.isEmpty() and cashier2.size < 5:
            cashier2.enQueue(main_queue.deQueue())

    # เพิ่มเวลาทั่วไป
    time += 1

    # พิมพ์สถานะปัจจุบัน
    print(f"{time} {main_queue} {cashier1} {cashier2}")