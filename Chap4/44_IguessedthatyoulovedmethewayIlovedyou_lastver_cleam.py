class Queue():
    def __init__(self):
        self.item_size = 0
        self.items = []

    @property
    def size(self):
        return self.item_size
    
    def deQueue(self):
        if self.item:
            self.item_size -= 1
            return self.items.pop(0)
        return "Empty"
    
    def enQueue(self, val):
        self.items.append(val)
        self.item_size += 1

    def isEmpty(self):
        return not self.items
    
    def __str__(self):
        return ", ".join(self.items)
    
    def actloc(self):
        activitys = {
            "0" : "Eat",
            "1" : "Game",
            "2" : "Learn",
            "3" : "Movie",
        }
        
        location = {
            "0" : "Res.",
            "1" : "ClassR.",
            "2" : "SuperM.",
            "3" : "Home"
        }

        res = ""
        for actloc in self.items:
            actloc.split(':')
            res += activitys[actloc.split(':')[0]]+":"+location[actloc.split(':')[1]]+", "
        return res[:-2]

inps = input("Enter Input : ").split(',')

q1 = Queue()
q2 = Queue()

score = 0
for inp in inps:
    my = inp.split()[0]
    your = inp.split()[1]
    my_act = my.split(':')[0]
    my_loc = my.split(':')[1]
    your_act = your.split(':')[0]
    your_loc = your.split(':')[1]

    if my_act == your_act and my_loc == your_loc:
        score += 4
    elif my_act == your_act:
        score += 1
    elif my_loc == your_loc:
        score += 2
    else:
        score -= 5
    
    q1.enQueue(my)
    q2.enQueue(your)

print(f"My   Queue = {q1}")
print(f"Your Queue = {q2}")

print(f"My   Activity:Location = {q1.actloc()}")
print(f"Your Activity:Location = {q2.actloc()}")

if score >= 7:
    print(f"Yes! You're my love! : Score is {score}.")
elif score > 0:
    print(f"Umm.. It's complicated relationship! : Score is {score}.")
else:
    print(f"No! We're just friends. : Score is {score}.")