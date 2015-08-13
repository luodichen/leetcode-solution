# https://leetcode.com/problems/subsets/
class Solution:
    def real_subsets(self, mainset, index, stack, result):
        tmp = list(stack)
        tmp.sort()
        result.append(tmp)
        
        for i in xrange(index, len(mainset)):
            stack.append(mainset[i])
            self.real_subsets(mainset, i + 1, stack, result)
            stack.pop()
    
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        stack = []
        result = []
        
        self.real_subsets(nums, 0, stack, result)
        return result
