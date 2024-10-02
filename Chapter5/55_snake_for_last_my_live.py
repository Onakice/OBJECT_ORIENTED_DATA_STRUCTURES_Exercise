class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next = None
        
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __str__(self):
        if self.isEmpty():
            return 'Empty'
        p = self.head
        result = f'({p.data})'
        if p.next == None:
            return result + '->Empty'
        while p.next != None:
            p = p.next
            result += '->' + str(p.data)
        return result
    
    def append(self, data):
        p = Node(data)
        if self.isEmpty():
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
        self.size += 1
        
    def isEmpty(self):
        return self.size == 0 or self.head == None
    
    def sum(self):
        result = 0
        p = self.head
        while p != None:
            result += int(p.data)
            p = p.next
        return result
        
    def SH(self):
        shaked_snake = Linkedlist()
        if self.isEmpty() or self.head.next == None:
            return shaked_snake
        
        prev = self.head
        cur = prev.next
        while cur != None:
            if int(cur.data) > int(self.head.data):
                shaked_snake.append(cur.data)
                prev.next = cur.next
                if cur == self.tail:
                    self.tail = prev
                self.size -= 1
            else:
                prev = cur
            cur = prev.next
        return shaked_snake
    
    def SW(self, inp1, inp2):
        inp1.data, inp2.data = inp2.data, inp1.data
    
    def D(self, snake_size):
        fall = Linkedlist()
        if self.sum() >= int(snake_size):
            return fall
        
        little_snake = None
        p = self.head
        while p != None:
            if int(p.data) != 0 and int(snake_size) % int(p.data) == 0 :
                little_snake = p
            p = p.next 
        
        if little_snake == None:
            self.SW(self.tail, self.head)
        else:
            s = little_snake.next
            while s != None:
                fall.append(s.data)
                self.size -= 1
                if s == self.tail:
                    break
                s = s.next
            little_snake.next = None
            self.tail = little_snake
            if self.size == 1:
                return 'Mom is dead'
        return fall
    
    def printList(self):
        if self.isEmpty():
            return '[]'
        result = ''
        p = self.head
        while p.next != None:
            result += str(p.data) + ', '
            p = p.next
        result += str(p.data)
        return f'[{result}]'

    def death(self):
        if self.head.next == None:
            return "Mom is dead"
    
linkedlist = Linkedlist()

inp = input("Snake Game : ")
child, ope = inp.split("/")
child = child.split()
mom = int(child[0])
child = list(map(int, child[1:]))
ope = ope.split(",")
linkedlist.append(mom)
for i in child:
    linkedlist.append(i)
print(linkedlist)

for i in ope:
    if linkedlist.death():
        print(linkedlist.death())
        break
    elif i[0] == 'D':
        result = linkedlist.D(i[2:])
        if result == 'Mom is dead':
            print(result)
            break
        else:
            print(f'Play success!->{result.printList()}')
            print(linkedlist)
    elif i == 'SH':
        result = linkedlist.SH()
        print(f'Shake success!->{result.printList()}')
        print(linkedlist)
    elif i == 'SW':
        prev = linkedlist.head
        cur = linkedlist.head.next
        if linkedlist.size >= 2:
            while cur != None and cur.next != None:
                linkedlist.SW(cur, cur.next)
                prev = cur.next
                cur = prev.next
        if cur != None:
            prev.next = None
            linkedlist.tail = prev
            linkedlist.size -= 1
        print('Swap success!')
        print(linkedlist)
    elif i[0] == 'F':
        linkedlist.append(i[2:])
        print(f'Steal success!->{i[2:]}')
        print(linkedlist)
    print('------------------------------')
else :
    if linkedlist.death():
        print(linkedlist.death())
print('Snake Game :')