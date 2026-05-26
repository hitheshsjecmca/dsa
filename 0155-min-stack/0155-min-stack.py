class MinStack(object):

    def __init__(self):
        self.s=[]
        self.ms=[]

    def push(self, val):
        self.s.append(val)
        if not self.ms or val<=self.ms[-1]:
            self.ms.append(val)
        

    def pop(self):
        if self.ms[-1]==self.s[-1]:
            self.ms.pop()

        self.s.pop()
        

    def top(self):
        return self.s[-1]
        

    def getMin(self):
        return self.ms[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()