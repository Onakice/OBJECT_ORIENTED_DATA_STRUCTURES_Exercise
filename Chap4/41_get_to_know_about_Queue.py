# class Queue:
#     def __init__(self):
#         pass

# queue = Queue()

# queue = []
# count_dequeue = 0

# inps = input("Enter Input : ").split(',')

# for inp in inps:
#     inp = inp.strip()
#     if inp.startswith('E'):
#         del_head, value = inp.split()
#         queue.append(value)
#         print(len(queue))
#     elif inp == 'D':
#         count_dequeue += 1
#         if count_dequeue != 0:
#             print(f"{queue[0]} 0")
#             queue.pop(0)
#         elif count_dequeue == 0:
#             print(f"{queue[0]} {queue[-1]}")
#             queue.pop(0)
#         print(count_dequeue)

def enqueue(value):
    queue.append(value)
    print(len(queue))

def dequeue():
    global count_dequeue
    if len(queue) == 0:
        print("-1")
        return
    
    front_value = queue.pop(0)
    if len(queue) != 0:
        print(f"{front_value} 0")
    else:
        print("Error")

def showqueue():
    if len(queue) == 0:
        print("Empty")
    else:
        print(" ".join(queue))


queue = []
count_dequeue = 0
            
inps = input("Enter Input : ").split(',')

for inp in inps:
    inp = inp.strip()
    if inp.startswith('E'):
        _, value = inp.split()
        enqueue(value)
    elif inp == 'D':
        dequeue()
showqueue()
    