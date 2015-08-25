# https://leetcode.com/problems/missing-number/
class Solution(object):
    def missingNumber(self, nums):
        ret = 0
        for i in xrange(len(nums)):
            ret += i - nums[i]
        
        ret += len(nums)
        
        return ret
