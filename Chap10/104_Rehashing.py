import math

# หาฟังก์ชันตรวจสอบว่าค่า num เป็น prime หรือไม่
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# หา prime ที่มากกว่าค่า n และใกล้ที่สุด
def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

# Quadratic probing สำหรับการหา index ใหม่
def quadratic_probe(table, size, key, attempt):
    return (key + attempt ** 2) % size

# Rehashing function
def rehash(table, data, max_collision, threshold):
    new_size = next_prime(2 * len(table))
    new_table = [None] * new_size
    print("****** Rehashing ******")
    
    for value in data:
        add_value(new_table, value, max_collision, threshold, data, rehashing=True)
        
    return new_table

# Function สำหรับการเพิ่มข้อมูลลงใน table
def add_value(table, value, max_collision, threshold, data, rehashing=False):
    size = len(table)
    key = value % size
    collision_count = 0
    attempt = 0
    
    while table[key] is not None:
        collision_count += 1
        if collision_count >= max_collision and not rehashing:
            print(f"collision number {collision_count} at {key}")
            print("****** Max collision - Rehash !!! ******")
            return rehash(table, data, max_collision, threshold)
        attempt += 1
        key = quadratic_probe(table, size, value, attempt)
    
    table[key] = value
    if not rehashing:
        data.append(value)
    
    if not rehashing:
        print(f"Add : {value}")
        if (len([x for x in table if x is not None]) / size) * 100 > threshold:
            print(f"****** Data over threshold - Rehash !!! ******")
            return rehash(table, data, max_collision, threshold)

    return table

# รับ input
input_data = input("Enter Input : ")
table_info, numbers_str = input_data.split('/')
table_size, max_collision, threshold = map(int, table_info.split())
numbers = list(map(int, numbers_str.split()))

# สร้าง table เริ่มต้น
table = [None] * table_size
data = []

print("Initial Table :")
for i in range(table_size):
    print(f"#{i+1}\tNone")

print("----------------------------------------")

# เพิ่มข้อมูลลงใน table
for num in numbers:
    table = add_value(table, num, max_collision, threshold, data)

# แสดงผลตารางหลังเพิ่มข้อมูล
print("----------------------------------------")
for i, val in enumerate(table):
    print(f"#{i+1}\t{val}")
