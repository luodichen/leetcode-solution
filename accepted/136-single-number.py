# https://leetcode.com/problems/single-number/
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        exists = set()
        result = set()
        
        for num in nums:
            if num not in exists:
                exists.add(num)
                result.add(num)
            else:
                result.remove(num)
        
        return result.pop()
