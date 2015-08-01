# https://leetcode.com/problems/min-stack/
class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if 0 == len(self.min_stack):
            self.min_stack.append(x)
        else:
            self.min_stack.append(x if x < self.min_stack[-1] else self.min_stack[-1])

    # @return nothing
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.min_stack[-1]
