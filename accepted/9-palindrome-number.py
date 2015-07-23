# https://leetcode.com/problems/palindrome-number/
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        mirr = 0
        orin = x
        
        while orin != 0:
            mirr *= 10
            mirr += orin % 10
            orin /= 10
        
        return mirr == x
