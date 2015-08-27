# https://leetcode.com/problems/next-permutation/
class Solution(object):
    def nextPermutation(self, nums):
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
            
        if i > 0:
            j = len(nums) - 1
            while j >= i and nums[j] <= nums[i - 1]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
        
        left = i
        right = len(nums) - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
