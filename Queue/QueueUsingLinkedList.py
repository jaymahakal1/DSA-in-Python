class EmptyQueueError(Exception):
    pass

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue:
    def __init__(self):
        self.qfront = None
        self.rear = None

    def isEmpty(self):
        if self.qfront == None and self.rear == None:
            return True
        return False
    
    def enqueue(self, val):
        node = Node(val)
        if self.isEmpty():
            self.qfront = node
            self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueError("Queue is Empty")
        
        if self.qfront.next == None:
            self.qfront = None
            self.rear = None
            return
        
        cur = self.qfront
        x = self.qfront.data
        self.qfront = self.qfront.next
        del cur
        return x
    
    def front(self):
        if self.isEmpty():
            raise EmptyQueueError("Queue is Empty")
        
        return self.qfront.data


        
q = Queue()

q.enqueue(1)
print(q.front())
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
