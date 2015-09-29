# https://leetcode.com/problems/find-the-duplicate-number/
class Solution(object):
    def findDuplicate(self, nums):
        lo, hi = 1, len(nums) - 1
        
        while hi - lo > 1:
            mid = (lo + hi) / 2
            lcount = 0
            
            for num in nums:
                if num <= mid:
                    lcount += 1
                
            if lcount > mid:
                hi = mid
            else:
                lo = mid
            
        count = 0
        for num in nums:
            if num == lo:
                count += 1
        
        return lo if count > 1 else hi
