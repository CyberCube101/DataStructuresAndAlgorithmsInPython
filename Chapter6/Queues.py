'''first into first out FIFO, but here we cannot use pop(0) as is this O(n)'''

from queue import Empty


class ArrayQueue:
    def __init__(self):
        self.data = []
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        self.data.append(e)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        answer = self.data[self.front]
        self.data[self.front] = None  # garbage collection
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return answer

    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self.data[self.front]


q = ArrayQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.data)
print(len(q))
print(q.dequeue())
q.enqueue(40)
print(q.first())
print(q.data)
print(q.dequeue())
