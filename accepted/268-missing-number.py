# https://leetcode.com/problems/missing-number/
class Solution(object):
    def missingNumber(self, nums):
        size = len(nums)
        i = 0
        
        while i < size:
            if nums[i] != i and nums[i] < len(nums):
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1
        
        for i in xrange(len(nums)):
            if i != nums[i]:
                return i
        
        return len(nums)
