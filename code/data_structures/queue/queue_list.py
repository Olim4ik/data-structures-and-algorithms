class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", queue.display())    # Output: Queue: [1, 2, 3]
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 1
# Output: Queue after dequeue: [2, 3]
print("Queue after dequeue:", queue.display())
print("Peek:", queue.peek())        # Output: Peek: 2
print("Queue size:", queue.size())  # Output: Queue size: 2
