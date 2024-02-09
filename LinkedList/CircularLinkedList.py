class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def insert_at_begining(self, data):
        node = Node(data)
        if self.last == None:
            self.last = node
            self.last.next = self.last
        else:
            front = self.last.next
            lst = self.last
            
            node.next = front
            lst.next = node

    def PrintList(self):
        lst = self.last
        if lst == None:
            print("List is Empty")
        else:
            front = self.last.next
            s = ''
            while front != lst:
                s += str(front.data)
                s += '--->'
                front = front.next
            s += str(front.data)
            print(s)

    def insert_at_end(self, data):
        node = Node(data)
        lst = self.last
        if lst == None:
            self.last = node
            self.last.next = self.last
        else:
            front = self.last.next
            lst.next = node
            node.next = front
            self.last = node
        
    def delete_from_begining(self):
        if self.last == None:
            print("List is Empty")
        elif self.last.next == self.last:
            self.last = None
        else:
            lst = self.last
            front = self.last.next
            lst.next = front.next
            del front

    def delete_from_end(self):
        if self.last == None:
            print("List is Empty")
        elif self.last.next == self.last:
            self.last = None
        else:
            front = self.last.next
            lst = self.last
            while front.next != self.last:
                front = front.next
            front.next = self.last.next
            self.last = front


start = CircularLinkedList()
start.insert_at_end(10)
start.insert_at_end(20)
start.insert_at_end(30)

start.PrintList()