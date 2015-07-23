#https://leetcode.com/problems/reverse-integer/
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        flag = False
        if x < 0:
            flag = True
            x = -x
        
        ret = 0
        while x != 0:
            ret *= 10
            ret += x % 10
            x /= 10
        
        
        ret = -ret if flag else ret
        
        return ret if (ret <= 2147483647 and ret >= -2147483648) else 0
