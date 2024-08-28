class FixedStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            return "Stack is full"
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_item = self.items[self.top]
        self.top -= 1
        return popped_item

    def peek(self):
        if not self.is_empty():
            return self.items[self.top]
        else:
            return "Stack is empty"

    def size(self):
        return self.top + 1

    def display(self):
        return self.items[:self.top + 1]


# Example usage:
stack = FixedStack(3)
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.display())  # Output: Stack: [1, 2, 3]
print("Pop:", stack.pop())        # Output: Pop: 3
print("Stack after pop:", stack.display())  # Output: Stack after pop: [1, 2]
print("Peek:", stack.peek())      # Output: Peek: 2
