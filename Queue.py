from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage
q = Queue()
q.enqueue("Person 1")
q.enqueue("Person 2")
print(f"Dequeue: {q.dequeue()}")
print(f"Dequeue: {q.dequeue()}")