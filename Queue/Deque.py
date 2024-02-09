class EmptyQueueException(Exception):
    pass

class Deque:
    def __init__(self, n):
        self.size = n
        self.front = -1
        self.rear = -1
        self.list = [0 for i in range(n)]

    def isEmpty(self):
        if self.front == -1:
            raise True
        return False
    
    def isFull(self):
        if (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1):
            return True
        return False
    
    def getRear(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is Empty")
        return self.list[self.rear]
    
    def getFront(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is Empty")
        return self.list[self.front]
    
    def pushFront(self, val):
        if self.isFull():
            return "Queue is Full"
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.front = (self.front + self.size - 1) % self.size

        self.list[self.front] = val
        return "Successfully inserted"
    
    def pushRear(self, val):
        if self.isFull():
            return "Queue is Full"
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear  = (self.rear + 1) % self.size

        self.list[self.rear] = val
        return "Successfully inserted"
    
    def popRear(self):
        if self.isEmpty():
            raise EmptyQueueException("queue is Empty")
        
        ans = self.list[self.rear]
        self.list[self.rear] = -1
        if self.front == self.rear: # single Element
            self.front = self.rear = -1
        else:
            self.rear = (self.rear + self.size - 1) % self.size
        return ans

    def popFront(self):
        if self.isEmpty():
            raise EmptyQueueException("queue is Empty")
        
        ans = self.list[self.front]
        self.list[self.front] = -1
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return ans
    
q = Deque(5)
print(q.pushFront(1))
print(q.popFront())