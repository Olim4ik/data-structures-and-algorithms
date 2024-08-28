class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.display())  # Output: Stack: [1, 2, 3]
print("Pop:", stack.pop())        # Output: Pop: 3
print("Stack after pop:", stack.display())  # Output: Stack after pop: [1, 2]
print("Peek:", stack.peek())      # Output: Peek: 2
print("Stack size:", stack.size())  # Output: Stack size: 2
