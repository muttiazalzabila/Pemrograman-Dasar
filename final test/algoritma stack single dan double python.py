class DoubleStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top1 = -1  # Stack kiri
        self.top2 = capacity  # Stack kanan

    def push1(self, item):
        if self.top1 + 1 < self.top2:
            self.top1 += 1
            self.stack[self.top1] = item
        else:
            print("Stack overflow")

    def push2(self, item):
        if self.top2 - 1 > self.top1:
            self.top2 -= 1
            self.stack[self.top2] = item
        else:
            print("Stack overflow")

    def pop1(self):
        if self.top1 >= 0:
            item = self.stack[self.top1]
            self.top1 -= 1
            return item
        return None

    def pop2(self):
        if self.top2 < self.capacity:
            item = self.stack[self.top2]
            self.top2 += 1
            return item
        return None

    def is_empty1(self):
        return self.top1 == -1

    def is_empty2(self):
        return self.top2 == self.capacity

# Contoh penggunaan
ds = DoubleStack(10)
ds.push1(1)
ds.push2(10)
ds.push1(2)
print(ds.pop1())  # Output: 2
print(ds.pop2())  # Output: 10
