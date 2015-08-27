# https://leetcode.com/problems/next-permutation/
class Solution(object):
    def nextPermutation(self, nums):
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
            
        if i > 0:
            l = i
            r = len(nums) - 1
            
            while r - l > 1:
                mid = (l + r) / 2
                if nums[i - 1] < nums[mid]:
                    l = mid
                else:
                    r = mid
            
            t = r if nums[i - 1] < nums[r] else l
            nums[i - 1], nums[t] = nums[t], nums[i - 1]
        
        left = i
        right = len(nums) - 1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
