# https://leetcode.com/problems/pascals-triangle/
class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        ret = []
        if numRows < 1:
            return ret
        
        ret.append([1, ])
        for i in xrange(1, numRows):
            node = [1, ]
            for j in xrange(1, i):
                node.append(ret[i - 1][j] + ret[i - 1][j - 1])
            node.append(1)
            ret.append(node)
        
        return ret
