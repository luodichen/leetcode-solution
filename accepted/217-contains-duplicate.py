# https://leetcode.com/problems/contains-duplicate/
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        
        return False
