# https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        ret = 0
        div = 5
        
        while n / div > 0:
            ret += n / div
            div *= 5
            
        return ret
