# https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        ret = 0
        for c in s:
            ret *= 26
            ret += ord(c) - ord('A') + 1
        
        return ret
