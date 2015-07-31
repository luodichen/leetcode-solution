# https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        ret = ""
        table = [chr(i + 64) if i > 0 else 'Z' for i in xrange(26)]
        while n > 0:
            ret = table[n % 26] + ret
            n = n / 26 if n % 26 > 0 else (n - 1) / 26
        
        return ret
