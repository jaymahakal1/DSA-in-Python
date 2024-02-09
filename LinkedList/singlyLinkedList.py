class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        itr = self.head
        if itr is None:
            self.head = node
        else:
            while itr.next is not None:
                itr = itr.next
            itr.next = node

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
            node.next = q
        else:
            node.next = self.head
            self.head = node

    def delete_from_begining(self):
        ptr = self.head
        if ptr is None:
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

    def ReverseList(self):
        prev = None
        cur = self.head
        fast = self.head
        while cur is not None:
            fast = cur.next
            cur.next = prev
            prev = cur
            cur = fast
        
        self.head = prev

    def BubbleSort(self):
        pass

    def hasCycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False

    def detectCycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                fast = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

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

    
start = SingleLinkedList()

start.insert_at_end(10)
start.insert_at_end(20)
start.insert_at_end(30)
start.insert_at_end(40)
start.insert_at_end(50)

# start.delete_from_begining()
# start.delete_from_begining()
# start.delete_from_begining()
# start.delete_from_begining()

start.PrintList()
# start.swapping()
# start.ReverseList()

# start.PrintList()

