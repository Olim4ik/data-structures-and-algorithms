from collections import deque


class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def is_empty(self):
        return len(self.queue1) == 0

    def push(self, item):
        self.queue2.append(item)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.queue1.popleft()

    def peek(self):
        if not self.is_empty():
            return self.queue1[0]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.queue1)

    def display(self):
        return list(self.queue1)


# Example usage:
stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.display())  # Output: Stack: [3, 2, 1]
print("Pop:", stack.pop())        # Output: Pop: 3
print("Stack after pop:", stack.display())  # Output: Stack after pop: [2, 1]
print("Peek:", stack.peek())      # Output: Peek: 2
