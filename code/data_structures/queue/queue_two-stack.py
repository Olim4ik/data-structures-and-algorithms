class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def display(self):
        if self.stack2:
            return self.stack2[::-1] + self.stack1
        return self.stack1


# Example usage:
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", queue.display())    # Output: Queue: [1, 2, 3]
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 1
# Output: Queue after dequeue: [2, 3]
print("Queue after dequeue:", queue.display())
print("Peek:", queue.peek())        # Output: Peek: 2
print("Queue size:", queue.size())  # Output: Queue size: 2
