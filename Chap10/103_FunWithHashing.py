class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class HashTable:
    def __init__(self, size, maxCollision):
        self.size = size
        self.maxCollision = maxCollision
        self.table = [None] * size # Create an empty table
        self.full_flag = False # Flag to track if the table is full

    def hashFunction(self, key):
        # Hash function: calculate the hash index by summing ASCII values of characters in the key
        return sum([ord(c) for c in key]) % self.size
    
    def insert(self, key, value):
        # Insert a key-value pair into the hash table, handling collisions with quadratic probing
        index = self.hashFunction(key)  # Get the hash index for the key
        collision = 0  # Track the number of collisions

        if self.table[index] is None:
            # If the slot is empty, insert the Data object
            self.table[index] = Data(key, value)
        else:
            # If collision occurs, apply quadratic probing to resolve it
            while self.table[index] is not None:
                collision += 1
                print(f"collision number {collision} at {index}")
                # Update the index using quadratic probing
                index = (self.hashFunction(key) + collision**2) % self.size
                if collision >= self.maxCollision:
                    # If maximum collisions are reached, print an error and stop
                    print("Max of collisionChain")
                    return  
            # Insert the Data object after resolving the collision
            self.table[index] = Data(key, value)

    def __str__(self):
        for i in range(self.size):
            if self.table[i] is None:
                print(f"#{i+1}\tNone")
            else:
                print(f"#{i+1}\t{self.table[i]}")
        return "---------------------------"

    def len(self):
        return len([i for i in self.table if i is not None])

print(" ***** Fun with hashing *****")
data = input("Enter Input : ").split("/")
size, maxCollision = map(int, data[0].split())
data = data[1].split(",")
table = HashTable(size, maxCollision)

for i in data:
    key, value = i.split()
    table.insert(key, value)
    print(table)
    if table.len() >= size and not table.full_flag:
        print("This table is full !!!!!!")
        exit() 