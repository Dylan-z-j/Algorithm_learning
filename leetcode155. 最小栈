import math

class MinStack:

    def __init__(self):
        self.stack = []
        self.min =  math.inf
    
    def push(self, x):
        self.stack.append(x)
        self.min = min(x, self.min)

    def pop(self):
        self.stack.pop()
        if self.stack:
            self.min = min(self.stack)
        else:
            self.min = math.inf

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
