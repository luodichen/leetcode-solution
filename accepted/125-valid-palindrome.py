# https://leetcode.com/problems/valid-palindrome/
class Solution:
    # @param {string} s
    # @return {boolean}
    def __init__(self):
        self.alphanum = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                             'u', 'v', 'w', 'x', 'y', 'z',
                             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        
    def isPalindrome(self, s):
        s = [c for c in s.lower() if c in self.alphanum]
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
