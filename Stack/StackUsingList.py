# stack
# push
# pop
# isempty
# peek

class Stack:
    def __init__(self):
        self.list = []

    def push(self, val):
        self.list.append(val)
        print("element pushed")

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            return self.list.pop()
            print("element poped")

    def isEmpty(self):
        return len(self.list) == 0

    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            return self.list[-1]
    

st = Stack()
st.pop()
st.push(1)
st.push(3)
print(st.peek())
