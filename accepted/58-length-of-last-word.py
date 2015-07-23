# https://leetcode.com/problems/length-of-last-word/
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        ret = 0
        cur = 0
        
        for c in s:
            cur = 0 if ' ' == c else (cur + 1)
            ret = cur if 0 != cur else ret
        
        return ret
