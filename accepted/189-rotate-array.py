# https://leetcode.com/problems/rotate-array/
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        len_nums = len(nums)
        k %= len_nums
        
        if 0 == k:
            return
        
        left = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = left
