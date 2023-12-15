class CircularQueue:
    def __init__(self, capacity): # constructor.
        self.capacity = capacity # Queue size
        self.queue = [None] * capacity 
        self.front = self.rear = -1 #Front and rear pointers

    def is_empty(self):
        return self.front == -1 # Queue empty

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front # Queue Full

    def enqueue(self, item): # Enqueue
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item

    def dequeue(self): # Dequeue
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
        else:
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity

    def peek(self): # First element
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
        else:
            return self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            i = self.front
            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.capacity
            print()

# Example usage:
cq = CircularQueue(5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()
cq.dequeue()
cq.enqueue(6)
cq.display() # 1 2 3 4 5 
