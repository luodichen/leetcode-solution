# https://leetcode.com/problems/combinations/
class Solution:
    def real_combine(self, stack, result, min, k, n):
        for i in xrange(min, n + 2 - k):
            stack.append(i)
            if 1 == k:
                result.append(list(stack))
            elif k > 1:
                self.real_combine(stack, result, i + 1, k - 1, n)
            stack.pop()
        
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        stack = []
        result = []
        self.real_combine(stack, result, 1, k, n)
        
        return result
