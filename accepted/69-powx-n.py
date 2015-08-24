# https://leetcode.com/problems/powx-n/
class Solution(object):
    def myPow(self, x, n):
        ret = 1.0
        cur = x
        
        negative = False
        if n < 0:
            n = -n
            negative = True
            cur = 1.0 / x
            
        while n != 0:
            if n & 1 != 0:
                ret *= cur
            
            cur = cur * cur
            n >>= 1
        
        return ret
