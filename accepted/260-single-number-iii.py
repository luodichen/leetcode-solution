# https://leetcode.com/problems/single-number-iii/
class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        
        div = 1
        while xor & div == 0:
            div <<= 1
            
        a = 0
        b = 0
        
        for num in nums:
            if num & div == 0:
                a ^= num
            else:
                b ^= num
        
        return [a, b, ]
