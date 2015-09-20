# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        if isBadVersion(1):
            return 1

        lo, hi = 1, n
        while hi - lo > 1:
            mid = (lo + hi) / 2
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid
        
        return hi
