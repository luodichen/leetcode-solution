# https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        m = {}
        
        for i in xrange(len(nums)):
            if nums[i] in m and i - m[nums[i]] <= k:
                return True
            else:
                m[nums[i]] = i
        
        return False
