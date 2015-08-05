# https://leetcode.com/problems/house-robber-ii/
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if nums is None or 0 == len(nums):
            return 0
        if len(nums) == 1:
            return nums[0]
        
        rub_first = (nums[0], nums[0], )
        not_rub_first = (nums[1], 0, )
        
        for i in xrange(2, len(nums) - 1):
            rubbed = rub_first[1] + nums[i]
            not_rubbed = rub_first[0] if rub_first[0] > rub_first[1] else rub_first[1]
            rub_first = (rubbed, not_rubbed, )
            
            rubbed = not_rub_first[1] + nums[i]
            not_rubbed = not_rub_first[0] if not_rub_first[0] > not_rub_first[1] else not_rub_first[1]
            not_rub_first = (rubbed, not_rubbed, )
            
        rub_last = nums[-1] + not_rub_first[1]
        tmp = rub_first[0] if rub_first[0] > rub_first[1] else rub_first[1]
        tmp = not_rub_first[0] if not_rub_first[0] > tmp else tmp
        not_rub_last = not_rub_first[1] if not_rub_first[1] > tmp else tmp
        
        return rub_last if rub_last > not_rub_last else not_rub_last
