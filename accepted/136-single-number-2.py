# https://leetcode.com/problems/single-number/
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        ret = 0
        for num in nums:
            ret ^= num
        return ret
