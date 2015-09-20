# https://leetcode.com/problems/move-zeroes/
class Solution(object):
    def moveZeroes(self, nums):
        lo = None
        
        for i in xrange(len(nums)):
            if lo is None and nums[i] == 0:
                lo = i
            elif lo is not None and nums[i] != 0:
                nums[lo], nums[i] = nums[i], 0
                lo += 1
