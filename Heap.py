class MinHeap:
    def __init__(self):
        self.list = [0] * 100005
        self.size = 0
        self.list[0] = -1
        #following 1 based indexing

    def insert(self, val):
        index = self.size + 1
        self.size += 1
        self.list[index] = val
        while index > 1:
            parent = index // 2
            if self.list[parent] > self.list[index]:
                self.list[parent], self.list[index] = self.list[index], self.list[parent]
            else:
                break

    def removeElement(self):
        if self.size == 0:
            return "Nothing to Remove"
        x = self.list[1]
        self.list[1] = self.list[self.size]
        self.size -= 1
        root = 1
        while True:
            left = 2 * root
            right = 2 * root + 1
            small = root
            if(left <= self.size and self.list[left] < self.list[small]):
                small = left
            
            if(right <= self.size and self.list[right] < self.list[small]):
                small = right

            if small != root:
                self.list[root], self.list[small] = self.list[small], self.list[root]
                root = small
            else:
                break

        return x

h = MinHeap()
h.insert(5)
h.insert(1)
h.insert(3)
h.insert(8)

for i in range(4):
    print(h.removeElement())
