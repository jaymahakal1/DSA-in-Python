class EmptyQueueError(Exception):
    pass

class CircularQueue:
    def __init__(self, n):
        self.list = [-1 for i in range(n)]
        self.size = n
        self.qfront = -1
        self.rear = -1

    def enqueue(self, val):
        if self.qfront == (self.rear + 1) % self.size :
            return "Queue is Full"
        elif self.qfront == -1:
            print(1)
            self.qfront = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.list[self.rear] = val
        return "Successfully added to queue"



    def dequeue(self):
        if self.qfront == -1:
            raise EmptyQueueError("Queue is Empty")
        else:
            ans = self.list[self.qfront]
            self.list[self.qfront] = -1
            self.qfront = (self.qfront + 1)%self.size
            return ans

    def front(self):
        if self.qfront == -1:
            raise EmptyQueueError("Queue is Empty")
        else:
            return self.list[self.qfront]


q = CircularQueue(6)
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))

print(q.enqueue(4))
print(q.enqueue(5))
print(q.enqueue(6))
print(q.enqueue(231))
print(q.enqueue(234))
print(q.dequeue())
print(q.dequeue())
print(q.enqueue(32))
print(q.enqueue(32))
print(q.enqueue(32))




