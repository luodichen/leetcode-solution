class Solution(object):
    def lengthOfLIS(self, nums):
        size = len(nums)
        if 0 == size:
            return 0
        
        dp = [0] * size
        dp[0] = 1
        
        for i in xrange(1, size):
            result = 1
            for j in xrange(i):
                if dp[j] >= result and nums[i] > nums[j]:
                    result = dp[j] + 1
            
            dp[i] = result
        
        return max(dp)
