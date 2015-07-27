# https://leetcode.com/problems/implement-queue-using-stacks/
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        tmp_stack = []
        while len(self.stack) > 0:
            tmp_stack.append(self.stack.pop())
        self.stack.append(x)
        while len(tmp_stack) > 0:
            self.stack.append(tmp_stack.pop())

    # @return nothing
    def pop(self):
        if len(self.stack) > 0:
            self.stack.pop()

    # @return an integer
    def peek(self):
        return self.stack[-1] if len(self.stack) > 0 else None

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0
