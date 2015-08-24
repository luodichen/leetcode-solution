# https://leetcode.com/problems/sqrtx/
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        
        lo = 0
        hi = x
        
        while hi - lo > 1:
            mid = (lo + hi) / 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                lo = mid
            else:
                hi = mid
        
        return lo
