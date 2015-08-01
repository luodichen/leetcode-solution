# https://leetcode.com/problems/valid-anagram/
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        
        for i in xrange(len(s)):
            if s[i] != t[i]:
                return False
        
        return True
