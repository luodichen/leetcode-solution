# https://leetcode.com/problems/permutations/
class Solution(object):
    def permute(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return [nums, ]
        
        ret = []
        for i in xrange(len(nums)):
            ret += [[nums[i]] + x for x in self.permute(nums[:i] + nums[i + 1:])]
        
        return ret
