class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        ptr = self.head
        node = Node(data)
        if ptr == None:
            self.head = node
        else:
            node.next = ptr
            ptr.prev = node
            self.head = node

    def insert_at_end(self, data):
        ptr = self.head
        node = Node(data)
        if ptr == None:
            self.head = node
        else:
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = node
            node.prev = ptr

    def insert_at_middle(self, data, cnt):
        node = Node(data)
        p = self.head
        if p is None:
            self.head = node
        elif cnt >= 1:
            c = 1
            while c < cnt:
                c += 1
                p = p.next

            q = p.next
            p.next = node
            node.prev = p
            node.next = q
            q.prev = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def PrintList(self):
        if self.head is None:
            print("List is Empty")
        else:
            itr = self.head
            st = ''
            while itr is not None:
                st += str(itr.data)
                st += '--->'
                itr = itr.next
            print(st)

    def ReverseTraversal(self):
        ptr = self.head
        s = ''
        while ptr.next != None:
            ptr = ptr.next

        while ptr != None:
            s += str(ptr.data)
            s += '--->'
            ptr = ptr.prev

        print(s)

    def delete_from_begining(self):
        ptr = self.head
        if ptr == None:
            print("List is Empty")
        else:
            q = ptr.next
            self.head = q
            del ptr
    
    def delete_from_end(self):
        prev = None
        ptr = self.head
        if ptr is None:
            print("List is Empty")
        elif ptr.next is None:
            del ptr
            self.head = None
        else:
            while ptr.next is not None:
                prev = ptr
                ptr = ptr.next
            del ptr
            prev.next = None

start = doublyLinkedList()
start.insert_at_end(10)
start.insert_at_end(20)

# for i in range(0,6):
#     start.delete_from_begining()
start.PrintList()
start.PrintList()
# start.ReverseTraversal()

