# https://leetcode.com/problems/implement-stack-using-queues/
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        tmp_queue = []
        tmp_queue.append(x)
        
        while 0 != len(self.queue):
            tmp_queue.append(self.queue.pop(0))
        self.queue = tmp_queue

    # @return nothing
    def pop(self):
        self.queue.pop(0)

    # @return an integer
    def top(self):
        return self.queue[0]

    # @return an boolean
    def empty(self):
        return 0 == len(self.queue)
