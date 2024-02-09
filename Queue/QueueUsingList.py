class EmptyQueueError(Exception):
    pass
class Queue:
    def __init__(self):
        self.list = []

    def push(self, value):
        self.list.append(value)
        print("Element Pushed")

    def pop(self):
        if self.isEmpty():
            return "queue is Empty"
        front  = self.list[0]
        # remember this operation is costly bcoz
        # after popping all elements has to be shifted left
        self.list.pop(0)

        return front
    
    def isEmpty(self):
        if len(self.list) == 0:
            return True
        return False


class queue:
    def __init__(self):
        self.size = 100001
        self.list = [-1 for i in range(0, 100001)]
        self.qfront = 0
        self.rear = 0
    
    def enqueue(self, val):
        if self.rear == self.size:
            print("Queue is Full")
            return
        self.list[self.rear] = val
        self.rear += 1

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueError("Queue is Empty")
        x = self.list[self.qfront]
        self.list[self.qfront] = -1
        self.qfront += 1
        if self.qfront == self.rear:
            self.qfront = 0
            self.rear = 0
        return x
    
    def front(self):
        if self.isEmpty():
            raise EmptyQueueError("Queue is Empty")
        return self.list[self.qfront]


    def isEmpty(self):
        if self.qfront == self.rear:
            return 1
        return 0
        

q = queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())

