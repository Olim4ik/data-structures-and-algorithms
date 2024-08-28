class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            return "Queue is full"
        if self.front == -1:  # First element to be enqueued
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        dequeued_item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.size == 0:  # Reset the queue when it becomes empty
            self.front = self.rear = -1
        return dequeued_item

    def peek(self):
        if not self.is_empty():
            return self.queue[self.front]
        else:
            return "Queue is empty"

    def size(self):
        return self.size

    def display(self):
        if self.is_empty():
            return []
        elif self.rear >= self.front:
            return self.queue[self.front:self.rear+1]
        else:  # Wrap around
            return self.queue[self.front:] + self.queue[:self.rear+1]


# Example usage:
queue = CircularQueue(3)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", queue.display())    # Output: Queue: [1, 2, 3]
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 1
queue.enqueue(4)
# Output: Queue after enqueue: [2, 3, 4]
print("Queue after enqueue:", queue.display())
print("Peek:", queue.peek())        # Output: Peek: 2
