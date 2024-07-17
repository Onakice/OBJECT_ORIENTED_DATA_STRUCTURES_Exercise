from collections import deque

class QueueSimulation:
    def __init__(self, people):
        self.main_queue = deque(people)
        self.cashier1_queue = deque()
        self.cashier2_queue = deque()
        self.cashier1_time = 3
        self.cashier2_time = 2
        self.time = 0
        
    def move_people(self):
        # Move people from main queue to cashiers if there is space
        if self.main_queue:
            if len(self.cashier1_queue) < 5:
                self.cashier1_queue.append(self.main_queue.popleft())
            elif len(self.cashier2_queue) < 5:
                self.cashier2_queue.append(self.main_queue.popleft())
        
    def process_cashiers(self):
        # Process cashier 1
        if self.cashier1_queue and self.time % self.cashier1_time == 0:
            self.cashier1_queue.popleft()
        
        # Process cashier 2
        if self.cashier2_queue and self.time % self.cashier2_time == 0:
            self.cashier2_queue.popleft()
        
    def simulate(self):
        while self.main_queue or self.cashier1_queue or self.cashier2_queue:
            self.time += 1
            
            # Move people to cashiers if there are people in the main queue
            self.move_people()
            
            # Process people at the cashiers
            self.process_cashiers()
            
            # Print current status
            print(f'{self.time} {list(self.main_queue)} {list(self.cashier1_queue)} {list(self.cashier2_queue)}')

# Input from the user
people = input("Enter people: ")

# Initialize the simulation with given people
simulation = QueueSimulation(list(people))

# Run the simulation
simulation.simulate()
