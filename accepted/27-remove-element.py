# https://leetcode.com/problems/remove-element/
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        result = [x for x in nums if x != val]
        del nums[::1]
        nums += result
        return len(nums)
