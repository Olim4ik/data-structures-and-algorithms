class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        return popped_node.data

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            return "Stack is empty"

    def size(self):
        return self._size

    def display(self):
        current = self.top
        items = []
        while current:
            items.append(current.data)
            current = current.next
        return items


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.display())  # Output: Stack: [3, 2, 1]
print("Pop:", stack.pop())        # Output: Pop: 3
print("Stack after pop:", stack.display())  # Output: Stack after pop: [2, 1]
print("Peek:", stack.peek())      # Output: Peek: 2
print("Stack size:", stack.size())  # Output: Stack size: 2
