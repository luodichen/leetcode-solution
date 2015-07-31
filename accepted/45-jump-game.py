# https://leetcode.com/problems/jump-game-ii/
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        size = len(nums)
        if size < 2:
            return 0
        
        min_jumps = [None, ] * size
        min_jumps[0] = 0
        farthest = 0
        
        for i in xrange(size):
            if i + nums[i] > farthest:
                end_position = i + nums[i] if i + nums[i] < size else size - 1
                for j in xrange(farthest + 1, end_position + 1):
                    min_jumps[j] = min_jumps[i] + 1
                if min_jumps[size - 1] is not None:
                    return min_jumps[size - 1]
                
                farthest = i + nums[i]
        
        return min_jumps[size - 1]
