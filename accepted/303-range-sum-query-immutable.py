# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):
    def __init__(self, nums):
        n = 0
        self.sum = [0] * (len(nums) + 1)
        for i in xrange(len(nums)):
            n += nums[i]
            self.sum[i + 1] = n

    def sumRange(self, i, j):
        return self.sum[j + 1] - self.sum[i]
