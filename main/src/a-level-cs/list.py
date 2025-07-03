# List (using Python's built-in list)
my_list = [1, 2, 3, 4]
my_list.remove(2)      # Remove value
print("List:", my_list)

# Stack (LIFO)
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None
    def peek(self):
        return self.items[-1] if self.items else None
    def is_empty(self):
        return len(self.items) == 0

# Queue (FIFO)
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0) if self.items else None
    def is_empty(self):
        return len(self.items) == 0

# Example usage
if __name__ == "__main__":
    # Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Stack pop:", stack.pop())

    # Queue
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print("Queue dequeue:", queue.dequeue())