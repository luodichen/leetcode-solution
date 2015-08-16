# https://leetcode.com/problems/largest-number/
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums.sort(cmp=lambda a, b: int(str(b) + str(a)) - int(str(a) + str(b)))
        return str(int(''.join([str(i) for i in nums])))
