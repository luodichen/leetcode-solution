# https://leetcode.com/problems/single-number-ii/
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        nums.sort()
        count = 1
        cur = nums[0]
        
        for i in xrange(1, len(nums)):
            if cur != nums[i]:
                if 3 != count:
                    return cur
                else:
                    cur = nums[i]
                    count = 1
            else:
                count += 1
        
        return cur
