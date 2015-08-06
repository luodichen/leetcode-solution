# https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def __init__(self):
        self.heap = None
    
    def sink(self, i):
        while i * 2 + 1 < len(self.heap):
            left = (i + 1) * 2 - 1
            right = (i + 1) * 2
            max = left if right >= len(self.heap) or self.heap[left] > self.heap[right] else right
            if self.heap[i] >= self.heap[max]:
                break
            else:
                tmp = self.heap[i]
                self.heap[i] = self.heap[max]
                self.heap[max] = tmp
                i = max
    
    def pop(self):
        if 0 == len(self.heap):
            return None
        
        ret = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.sink(0)
        else:
            self.heap.pop()
        
        return ret
        
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        self.heap = nums
        for i in xrange(len(nums) / 2, -1, -1):
            self.sink(i)
        
        ret = None
        for i in xrange(k):
            ret = self.pop()
        
        return ret
