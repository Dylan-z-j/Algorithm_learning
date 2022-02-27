## 用两个栈实现一个队列

class CQueue:

    def __init__(self):

        self.left_stack = []
        self.right_stack = []

    def appendTail(self, value: int) -> None:

        self.right_stack.append(value)
        self.left_stack = []
        temp_stack = copy.deepcopy(self.right_stack)
        while temp_stack != []:
            self.left_stack.append(temp_stack.pop())

    def deleteHead(self) -> int:
        if len(self.left_stack) == 0:
            return -1
        else:
            res =  self.left_stack.pop()
            self.right_stack = []
            temp_stack = copy.deepcopy(self.left_stack)
            while len(temp_stack) != 0:
                self.right_stack.append(temp_stack.pop())
            return res



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
