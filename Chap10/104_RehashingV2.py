class HashTable:
    def __init__(self, size, max_col, threshold):
        self.size = size
        self.max_col = max_col
        self.threshold = threshold
        self.table = [None] * size  # Empty table
        self.data_count = 0  # Count of inserted data
        self.add_list = set() # Track inserted keys

    def insert(self, key):
        # Insert a key into the hash table using quadratic probing for collisions
        index = key % self.size  # Calculate hash index
        init_index = index  # Store initial index for probing
        col = 0  # Collision counter

        while col < self.max_col:
            if self.table[index] is None:
                # Insert key if spot is empty
                self.table[index] = key
                self.data_count += 1
                self.add_list.add(key)
                return True
            else:
                # Handle collision with quadratic probing
                col += 1
                print(f"collision number {col} at {index}")
                if col >= self.max_col:
                    # Max collisions reached, trigger rehash
                    print("****** Max collision - Rehash !!! ******")
                    return False
                index = (init_index + col ** 2) % self.size  # Quadratic probing
        return False

    def is_over(self):
        # Check if the table is over the specified threshold (percentage of table filled)
        percent = (self.data_count + 1) / self.size * 100
        if percent >= self.threshold:
            # If the percentage exceeds the threshold, trigger rehashing
            print("****** Data over threshold - Rehash !!! ******")
            return True
        return False

    def rehash(self):
        # Rehash the table by increasing its size and re-inserting all keys
        self.size = self.get_prime(self.size * 2)  # Double the table size and find the next prime
        self.table = [None] * self.size  # Create a new, empty table
        self.data_count = 0  # Reset the data count
        for key in self.add_list:
            # Re-insert all previously added keys
            self.insert(key)

    def get_prime(self, n):
        # Find the next prime number greater than or equal to n
        def is_prime(num):
            # Helper function to check if a number is prime
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        prime = n
        while True:
            if is_prime(prime):
                return prime
            prime += 1

    def print_table(self):
        # Print the current state of the hash table
        for i in range(self.size):
            value = self.table[i]
            print(f"#{i + 1}\t{value if value is not None else 'None'}")
        print("----------------------------------------")

    def add_data(self, key):
        # Add data to the hash table, check if rehashing is needed, and print the table
        print(f"Add : {key}")
        if self.is_over():
            # If the table is over the threshold, rehash
            self.rehash()
        inserted = self.insert(key)
        if not inserted:
            # If insertion fails due to collisions, rehash and try again
            self.rehash()
            self.insert(key)
        self.print_table()  # Print the updated table

print(" ***** Rehashing *****")
inp = input("Enter Input : ").split('/')
table_info = list(map(int, inp[0].split()))
table_size = table_info[0]
max_collision = table_info[1]
threshold = table_info[2]
data = list(map(int, inp[1].split()))

hash_table = HashTable(table_size, max_collision, threshold)
print("Initial Table :")
hash_table.print_table()

for key in data:
    hash_table.add_data(key)