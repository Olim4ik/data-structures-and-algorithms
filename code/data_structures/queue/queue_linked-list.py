class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        dequeued_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self._size -= 1
        return dequeued_node.data

    def peek(self):
        if not self.is_empty():
            return self.front.data
        else:
            return "Queue is empty"

    def size(self):
        return self._size

    def display(self):
        current = self.front
        items = []
        while current:
            items.append(current.data)
            current = current.next
        return items


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
