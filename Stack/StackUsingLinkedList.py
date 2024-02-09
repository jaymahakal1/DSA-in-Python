class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        print("element Pushed")

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return
        prev = self.top.next
        cur = self.top
        x = self.top.data
        del cur
        self.top = prev
        return x

    def isEmpty(self):
        if self.top == None:
            return True
        return False


st = Stack()
st.pop()
st.push(1)
st.push(2)
st.push(3)
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())