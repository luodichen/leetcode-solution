# https://leetcode.com/problems/maximum-gap/
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        size = len(nums)
        if size < 2:
            return 0
        
        max = nums[0]
        min = nums[0]
        
        for i in xrange(1, size):
            if nums[i] > max:
                max = nums[i]
            if nums[i] < min:
                min = nums[i]
        
        buckets = [None, ] * size
        bucket_size = (max - min + size) / size
        
        for num in nums:
            index = (num - min) / bucket_size
            if buckets[index] is None:
                buckets[index] = [num, num, ]
            elif num < buckets[index][0]:
                buckets[index][0] = num
            elif num > buckets[index][1]:
                buckets[index][1] = num
        
        ret = 0
        prev = buckets[0][1]
        
        for i in xrange(1, size):
            if buckets[i] is not None:
                ret = buckets[i][0] - prev if buckets[i][0] - prev > ret else ret
                prev = buckets[i][1]
        
        return ret
