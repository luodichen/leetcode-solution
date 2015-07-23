# https://leetcode.com/problems/majority-element/
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        count_map = {}
        nums_len = len(nums)
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        for (k, v) in count_map.items():
            if v > nums_len / 2:
                return k
