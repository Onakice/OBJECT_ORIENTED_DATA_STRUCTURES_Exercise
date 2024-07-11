def enqueue(value):
    queue.append(value)
    print(len(queue))

def dequeue():
    global count_dequeue
    if len(queue) == 0:
        print("-1")
        return
    
    front_value = queue.pop(0)
    print(f"{front_value} 0")

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
    