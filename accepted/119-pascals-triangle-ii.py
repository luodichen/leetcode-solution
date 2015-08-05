# https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        ret = [1] * (rowIndex + 1)
        
        for i in xrange(1, rowIndex + 1):
            prev = 1
            for j in xrange(1, i):
                tmp = prev + ret[j]
                prev = ret[j]
                ret[j] = tmp
        
        return ret
